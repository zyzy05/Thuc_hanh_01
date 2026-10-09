import json
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"
DEVICE_ID = "light01"
light_status = "OFF"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Smart Light da ket noi MQTT broker!")
        client.subscribe(CMD_TOPIC)
        print(f"Dang cho lenh tai: {CMD_TOPIC}")
    else:
        print(f"Ket noi that bai: {reason_code}")


def on_message(client, userdata, message):
    global light_status
    command = message.payload.decode("utf-8").strip().upper()
    print(f"\\nNhan lenh: {command}")

    if command == "ON":
        light_status = "ON"
    elif command == "OFF":
        light_status = "OFF"
    else:
        print("Lenh khong hop le, bo qua.")
        return

    status_data = {"device_id": DEVICE_ID, "status": light_status}
    payload = json.dumps(status_data, ensure_ascii=False)
    client.publish(STATUS_TOPIC, payload, qos=0)
    print(f"Da cap nhat trang thai: {light_status}")
    print(f"Da gui phan hoi: {payload}")


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="device_bai3_light01"
)
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(BROKER, PORT, 60)
    print("Nhan Ctrl+C de dung Smart Light Device.")
    client.loop_forever()
except KeyboardInterrupt:
    print("\\nDa dung Smart Light Device.")
except Exception as error:
    print(f"Loi: {error}")
finally:
    client.disconnect()
