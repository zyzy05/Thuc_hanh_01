from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/lab/message"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Da ket noi MQTT broker thanh cong!")
        client.subscribe(TOPIC)
        print(f"Dang lang nghe topic: {TOPIC}")
    else:
        print(f"Ket noi that bai: {reason_code}")


def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8", errors="replace")
    thoi_gian = datetime.now().strftime("%H:%M:%S")
    print("\\nNhan duoc message:")
    print(f"Topic: {message.topic}")
    print(f"Payload: {payload}")
    print(f"Time: {thoi_gian}")
    print("-" * 40)


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="subscriber_bai1_student"
)
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(BROKER, PORT, 60)
    print("Nhan Ctrl+C de dung Subscriber.")
    client.loop_forever()
except KeyboardInterrupt:
    print("\\nDa dung Subscriber.")
except Exception as error:
    print(f"Loi: {error}")
finally:
    client.disconnect()
