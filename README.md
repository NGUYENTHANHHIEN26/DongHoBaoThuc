# ⏰ Đồng Hồ Báo Thức Thông Minh Nhận Biết Chuyển Động

Ứng dụng đồng hồ báo thức thông minh được phát triển bằng **Python**, tích hợp giao diện đồ họa trực quan (`tkinter`), xử lý đa luồng (`threading`) và tính năng mô phỏng chuyển động độc đáo thông qua phím bấm bàn phím (`keyboard`, `winsound`).

🔗 **Repository GitHub:** [https://github.com/NGUYENTHANHHIEN26/DongHoBaoThuc](https://github.com/NGUYENTHANHHIEN26/DongHoBaoThuc)

---

## 🌟 Tính năng nổi bật

* **🕐 Đồng hồ thời gian thực:** Hiển thị giờ, phút, giây cập nhật liên tục từng giây, đảm bảo giao diện luôn sống động và chính xác.
* **⏰ Quản lý báo thức thông minh:** Cho phép người dùng nhập mốc thời gian hẹn giờ theo định dạng `HH:MM`, đặt lịch dễ dàng và chủ động dừng chuông khi đến giờ.
* **🕹️ Mô phỏng chuyển động qua phím "A":**
  * Nhấn phím `A` để kích hoạt hiệu ứng giả lập chuyển động.
  * Số lần nhấn phím sẽ quyết định số tiếng bíp phát ra tăng dần (Lần 1 = 2 tiếng, lần 2 = 3 tiếng,...).
  * Tần số và độ trễ âm thanh thay đổi tự động theo nhịp thao tác, tạo cảm giác tăng tốc sinh động.
* **🧵 Kiến trúc đa luồng (Multithreading):** Phân tách hoàn toàn luồng giao diện GUI, luồng kiểm tra thời gian, luồng phát âm thanh báo thức và luồng lắng nghe bàn phím, giúp ứng dụng vận hành mượt mà, hoàn toàn không xảy ra tình trạng đứng hình (`not responding`).

---

## 🛠️ Công nghệ & Thư viện sử dụng

* **Ngôn ngữ:** Python 3.x
* **Thư viện chuẩn & bên thứ ba:**
  * `tkinter`: Xây dựng giao diện người dùng đồ họa (GUI).
  * `threading`: Xử lý đa luồng đồng thời các tác vụ ngầm.
  * `time`: Quản lý thời gian thực và thiết lập độ trễ tín hiệu.
  * `winsound`: Xử lý và phát âm thanh tiếng bíp (hỗ trợ Windows).
  * `keyboard`: Lắng nghe sự kiện bàn phím toàn hệ thống.

---

## ⚙️ Hướng dẫn cài đặt và chạy chương trình

### 1. Cài đặt thư viện phụ thuộc
Mở terminal/cmd và cài đặt thư viện `keyboard`:
```bash
pip install keyboard
```
*(Lưu ý trên hệ điều hành Windows, bạn có thể cần chạy terminal dưới quyền **Administrator** để thư viện `keyboard` lắng nghe phím toàn hệ thống chính xác).*

### 2. Chạy ứng dụng
Tải mã nguồn về máy và chạy lệnh sau tại thư mục chứa file:
```bash
python donghobaothuc.py
```

---

## 📂 Cấu trúc dự án

```text
📦 DongHoBaoThuc
 ┣ 📜 donghobaothuc.py  # Mã nguồn chính (Giao diện + Luồng + Âm thanh)
 ┗ 📜 README.md         # Tài liệu hướng dẫn dự án
```

---

## 👩‍💻 Tác giả
* **Nguyễn Thanh Hiền**
