import json
import random
import time
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"
DEVICE_ID = "sensor01"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Sensor da ket noi MQTT broker!")
    else:
        print(f"Ket noi that bai: {reason_code}")


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="sensor_publisher_bai2_student"
)
client.on_connect = on_connect

try:
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    time.sleep(1)

    while True:
        data = {
            "device_id": DEVICE_ID,
            "temperature": round(random.uniform(20.0, 40.0), 1),
            "humidity": round(random.uniform(30.0, 90.0), 1)
        }
        payload = json.dumps(data, ensure_ascii=False)
        info = client.publish(TOPIC, payload, qos=0)
        info.wait_for_publish()
        print(f"Da gui du lieu: {payload}")
        time.sleep(3)

except KeyboardInterrupt:
    print("\\nDa dung Sensor Publisher.")
except Exception as error:
    print(f"Loi: {error}")
finally:
    client.loop_stop()
    client.disconnect()
