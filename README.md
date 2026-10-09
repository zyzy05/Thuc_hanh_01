# THỰC HÀNH 01: LẬP TRÌNH PYTHON VỚI GIAO THỨC MQTT

## 1. Giới thiệu

Bài thực hành giúp sinh viên làm quen với giao thức MQTT (Message Queuing Telemetry Transport) và mô hình giao tiếp Publisher/Subscriber trong các hệ thống IoT.

Trong bài này, Python được sử dụng để xây dựng hai chương trình:

* **Publisher:** Kết nối tới MQTT Broker và gửi thông điệp lên một topic.
* **Subscriber:** Đăng ký lắng nghe topic, nhận thông điệp và hiển thị nội dung cùng thời điểm nhận.

## 2. Mục tiêu

Sau khi hoàn thành bài thực hành, sinh viên có thể:

* Hiểu cách một ứng dụng Python kết nối tới MQTT Broker.
* Biết cách gửi và nhận thông điệp bằng MQTT.
* Hiểu vai trò của Publisher, Subscriber, Broker, Topic và Payload.
* Biết cách sử dụng thư viện `paho-mqtt` trong Python.
* Vận dụng MQTT để mô phỏng giao tiếp giữa các thiết bị IoT.

## 3. Môi trường thực hành

* Ngôn ngữ lập trình: Python 3.x
* Thư viện: `paho-mqtt`
* IDE: Visual Studio Code
* MQTT Broker: `test.mosquitto.org`
* Port: `1883`
* Giao thức kết nối: MQTT qua TCP

### Cài đặt thư viện

Mở Terminal tại thư mục dự án và chạy lệnh:

```bash
python -m pip install paho-mqtt
```

Có thể kiểm tra thư viện đã được cài đặt bằng lệnh:

```bash
python -m pip show paho-mqtt
```

## 4. Cấu trúc chương trình

```text
python-mqtt-lab/
├── publisher_bai1.py
├── subscriber_bai1.py
├── sensor_publisher_bai2.py
├── monitor_subscriber_bai2.py
├── device_bai3.py
├── controller_bai3.py
├── requirements.txt
└── README.md
```

Trong phạm vi thực hành 01, hai file được sử dụng là:

* `publisher_bai1.py`: Chương trình gửi thông điệp MQTT.
* `subscriber_bai1.py`: Chương trình nhận thông điệp MQTT.

## 5. Cấu hình MQTT Broker

Các thông số kết nối được khai báo trong hai chương trình:

| Thông số | Giá trị              |
| -------- | -------------------- |
| Broker   | `test.mosquitto.org` |
| Port     | `1883`               |
| Topic    | `iot/lab/message`    |
| Username | Không yêu cầu        |
| Password | Không yêu cầu        |

Đây là broker công khai phục vụ mục đích thử nghiệm. Cần có kết nối Internet để sử dụng. Không gửi dữ liệu cá nhân hoặc thông tin nhạy cảm qua broker này.

## 6. Nội dung thực hành

### 6.1. Chương trình Publisher

File: `publisher_bai1.py`

Chức năng:

1. Kết nối tới MQTT Broker.
2. Nhập họ tên và mã sinh viên.
3. Nhập nội dung thông điệp cần gửi.
4. Publish thông điệp lên topic `iot/lab/message`.
5. Cho phép gửi nhiều thông điệp liên tiếp.
6. Nhập `EXIT` để kết thúc chương trình.

Payload được gửi có dạng:

```text
Xin chao tu client Python MQTT - B23DCCN001 - Nguyen Van A
```

Trong đó, mã sinh viên và họ tên cần được thay bằng thông tin thực tế của người thực hiện.

### 6.2. Chương trình Subscriber

File: `subscriber_bai1.py`

Chức năng:

1. Kết nối tới cùng MQTT Broker.
2. Subscribe topic `iot/lab/message`.
3. Chờ nhận thông điệp từ Publisher.
4. Hiển thị topic, nội dung và thời điểm nhận thông điệp.
5. Tiếp tục chạy cho đến khi người dùng nhấn `Ctrl + C`.

## 7. Hướng dẫn chạy chương trình

### Bước 1: Mở Terminal thứ nhất

Trong Visual Studio Code, chọn **Terminal → New Terminal**.

Chạy Subscriber trước:

```bash
python subscriber_bai1.py
```

Khi kết nối thành công, chương trình sẽ thông báo đang lắng nghe topic `iot/lab/message`.

### Bước 2: Mở Terminal thứ hai

Chọn dấu `+` trong khu vực Terminal để mở một Terminal mới.

Chạy Publisher:

```bash
python publisher_bai1.py
```

### Bước 3: Nhập thông tin và gửi thông điệp

Ví dụ:

```text
Nhap ho ten: Nguyen Van A
Nhap ma sinh vien: B23DCCN001
Nhap loi chao (EXIT de thoat): Xin chao tu client Python MQTT
```

### Bước 4: Kiểm tra kết quả

Nếu kết nối và truyền dữ liệu thành công, Subscriber sẽ hiển thị thông tin tương tự:

```text
Nhan duoc message:
Topic: iot/lab/message
Payload: Xin chao tu client Python MQTT - B23DCCN001 - Nguyen Van A
Time: 10:15:20
```

Thời điểm nhận thực tế phụ thuộc vào thời gian chạy chương trình.

### Bước 5: Kết thúc chương trình

* Publisher: Nhập `EXIT`.
* Subscriber: Nhấn `Ctrl + C`.

## 8. Kết quả đạt được

Sau khi hoàn thành bài thực hành:

* Publisher kết nối được với MQTT Broker.
* Publisher gửi thông điệp lên đúng topic `iot/lab/message`.
* Subscriber đăng ký topic và nhận được thông điệp.
* Subscriber hiển thị được topic, payload và thời điểm nhận.
* Hai chương trình giao tiếp được với nhau thông qua MQTT Broker.

## 9. Một số lỗi thường gặp

### Lỗi chưa cài thư viện

Thông báo:

```text
ModuleNotFoundError: No module named 'paho'
```

Cách khắc phục:

```bash
python -m pip install paho-mqtt
```

### Subscriber không nhận được thông điệp

Kiểm tra:

* Subscriber đã chạy trước Publisher chưa.
* Topic trong hai chương trình có giống nhau không.
* Hai chương trình có kết nối tới cùng Broker không.
* Kết nối Internet có hoạt động không.

Do sử dụng broker công khai, có thể có thông điệp từ những người dùng khác cùng sử dụng topic. Khi cần thử nghiệm riêng, nên thay topic bằng một tên riêng có thêm mã sinh viên và cập nhật đồng bộ ở cả Publisher lẫn Subscriber.

## 10. Kết luận

Bài thực hành 01 giúp sinh viên hiểu và triển khai được mô hình Publisher/Subscriber bằng Python với giao thức MQTT. Đây là kiến thức nền tảng để tiếp tục thực hiện các bài thực hành về mô phỏng cảm biến và điều khiển thiết bị IoT.
