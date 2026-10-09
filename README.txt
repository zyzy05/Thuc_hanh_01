BAI THUC HANH PYTHON MQTT
=========================

1. GIOI THIEU
Du an gom 3 bai thuc hanh lap trinh Python voi giao thuc MQTT:
- Bai 1: Gui va nhan thong diep MQTT.
- Bai 2: Mo phong cam bien nhiet do va do am.
- Bai 3: Dieu khien den thong minh qua MQTT.

2. MOI TRUONG
- Python 3.x
- Thu vien paho-mqtt
- IDE: Visual Studio Code
- MQTT Broker: test.mosquitto.org
- Port: 1883
- Giao thuc: MQTT TCP (khong TLS)

3. CAI DAT
Mo Terminal tai thu muc du an va chay:
python -m pip install -r requirements.txt

Neu dung python3:
python3 -m pip install -r requirements.txt

4. CHAY BAI 1
Mo hai Terminal.

Terminal 1:
python subscriber_bai1.py

Terminal 2:
python publisher_bai1.py

Publisher gui thong diep len topic iot/lab/message.
Subscriber hien thi topic, payload va thoi diem nhan.
Nhap EXIT trong Publisher de ket thuc; Ctrl+C de dung Subscriber.

5. CHAY BAI 2
Mo hai Terminal.

Terminal 1:
python monitor_subscriber_bai2.py

Terminal 2:
python sensor_publisher_bai2.py

Sensor Publisher gui du lieu JSON moi 3 giay len topic:
iot/lab/sensor01/data

Monitoring Subscriber hien thi du lieu va canh bao khi:
- Nhiet do > 35 do C
- Do am < 40%

6. CHAY BAI 3
Mo hai Terminal.

Terminal 1:
python device_bai3.py

Terminal 2:
python controller_bai3.py

Controller gui ON hoac OFF len topic:
iot/lab/light01/cmd

Thiet bi cap nhat trang thai va gui JSON len topic:
iot/lab/light01/status

Nhap EXIT de ket thuc Controller.

7. KET QUA MONG DOI
- Bai 1: Publish va subscribe thong diep MQTT.
- Bai 2: Gui/nhan JSON cam bien va hien thi canh bao theo nguong.
- Bai 3: Dieu khien den va nhan phan hoi trang thai qua MQTT.

8. LUU Y
- Can co ket noi Internet de truy cap broker.
- Broker cong khai chi dung cho muc dich hoc tap; khong gui du lieu rieng tu.
- Hay chay chuong trinh nhan truoc chuong trinh gui.
- Neu nhieu nguoi dung chung broker, co the nhan duoc thong diep tu nguoi khac.
- Co the thay topic bang topic rieng co them ma sinh vien, nhung phai sua dong bo
  topic o ca chuong trinh publish va subscribe.
- Neu gap loi CallbackAPIVersion, cap nhat bang:
  python -m pip install --upgrade paho-mqtt
