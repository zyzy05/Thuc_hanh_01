import json
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Monitoring da ket noi MQTT broker!")
        client.subscribe(TOPIC)
        print(f"Dang theo doi: {TOPIC}")
    else:
        print(f"Ket noi that bai: {reason_code}")


def on_message(client, userdata, message):
    try:
        payload = message.payload.decode("utf-8")
        data = json.loads(payload)
        device_id = data["device_id"]
        temperature = float(data["temperature"])
        humidity = float(data["humidity"])

        print("\\n===== DU LIEU CAM BIEN =====")
        print(f"Device: {device_id}")
        print(f"Temperature: {temperature:.1f} C")
        print(f"Humidity: {humidity:.1f} %")
        if temperature > 35:
            print("CANH BAO: Nhiet do cao")
        if humidity < 40:
            print("CANH BAO: Do am thap")
        print("=" * 30)
    except (ValueError, TypeError, KeyError) as error:
        print(f"Du lieu khong hop le: {error}")


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="monitor_subscriber_bai2_student"
)
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(BROKER, PORT, 60)
    print("Nhan Ctrl+C de dung Monitoring Subscriber.")
    client.loop_forever()
except KeyboardInterrupt:
    print("\\nDa dung Monitoring Subscriber.")
except Exception as error:
    print(f"Loi: {error}")
finally:
    client.disconnect()
