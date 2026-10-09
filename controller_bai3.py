import json
import threading
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"
connected_event = threading.Event()


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Controller da ket noi MQTT broker!")
        client.subscribe(STATUS_TOPIC)
        connected_event.set()
        print(f"Dang theo doi: {STATUS_TOPIC}")
    else:
        print(f"Ket noi that bai: {reason_code}")


def on_message(client, userdata, message):
    try:
        payload = message.payload.decode("utf-8")
        data = json.loads(payload)
        print("\\nTrang thai nhan duoc:")
        print(json.dumps(data, ensure_ascii=False))
        print(f"Thiet bi: {data['device_id']}")
        print(f"Trang thai den: {data['status']}")
    except (ValueError, TypeError, KeyError) as error:
        print(f"Phan hoi khong hop le: {error}")


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="controller_bai3_student"
)
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    if not connected_event.wait(timeout=10):
        raise TimeoutError("Khong the ket noi MQTT broker.")

    while True:
        command = input("\\nNhap lenh (ON/OFF/EXIT): ").strip().upper()
        if command == "EXIT":
            break
        if command not in ("ON", "OFF"):
            print("Lenh khong hop le. Chi nhap ON, OFF hoac EXIT.")
            continue

        info = client.publish(CMD_TOPIC, command, qos=0)
        info.wait_for_publish()
        print(f"Da gui lenh {command} toi light01")

except KeyboardInterrupt:
    print("\\nDa dung Controller.")
except Exception as error:
    print(f"Loi: {error}")
finally:
    client.loop_stop()
    client.disconnect()
