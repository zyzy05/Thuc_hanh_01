import time
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/lab/message"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Da ket noi MQTT broker thanh cong!")
    else:
        print(f"Ket noi that bai: {reason_code}")


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="publisher_bai1_student"
)
client.on_connect = on_connect

try:
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    time.sleep(1)

    ho_ten = input("Nhap ho ten: ").strip()
    ma_sinh_vien = input("Nhap ma sinh vien: ").strip()

    if not ho_ten or not ma_sinh_vien:
        print("Ho ten va ma sinh vien khong duoc de trong.")
    else:
        while True:
            noi_dung = input("Nhap loi chao (EXIT de thoat): ").strip()
            if noi_dung.upper() == "EXIT":
                break
            if not noi_dung:
                print("Noi dung khong duoc de trong.")
                continue

            payload = f"{noi_dung} - {ma_sinh_vien} - {ho_ten}"
            info = client.publish(TOPIC, payload, qos=0)
            info.wait_for_publish()
            print(f"Da gui: {payload}")
            print(f"Topic: {TOPIC}")

except KeyboardInterrupt:
    print("\\nDa dung Publisher.")
except Exception as error:
    print(f"Loi: {error}")
finally:
    client.loop_stop()
    client.disconnect()
