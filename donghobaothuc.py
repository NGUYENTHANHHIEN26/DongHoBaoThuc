import tkinter as tk, threading, time, keyboard, winsound

alarm_time, alarm_on, stop_flag, thread_bip = None, False, False, None
count_press = 0     # đếm số lần nhấn phím A

# --- Phát tiếng bíp tăng dần (báo thức) ---
def phat_bip():
    global stop_flag
    stop_flag = False
    delay, freq = 0.5, 1200
    while not stop_flag:
        winsound.Beep(freq, 400)
        time.sleep(delay)
        freq = min(freq + 50, 2000)
        delay = max(delay - 0.02, 0.05)

# --- Thử bíp phím A: lần đầu 2 tiếng, lần sau tăng dần ---
def lang_nghe_phim():
    global count_press
    while True:
        if keyboard.is_pressed("a"):
            count_press += 1

            so_tieng_bip = count_press + 1   # lần 1 = 2 tiếng, lần 2 = 3 tiếng…

            for _ in range(so_tieng_bip):
                winsound.Beep(1500, 200)
                time.sleep(0.15)

            # tránh bị lặp khi giữ phím
            time.sleep(0.35)

        time.sleep(0.05)

# --- Dừng bíp ---
def dung_bip():
    global stop_flag
    stop_flag = True
    label_status.config(text="🛑 Báo thức đã dừng", fg="red")

# --- Đặt báo thức ---
def dat_bao_thuc():
    global alarm_time, alarm_on, thread_bip
    alarm_time = entry.get().strip()
    if not alarm_time:
        label_status.config(text="⚠️ Nhập HH:MM", fg="orange")
        return
    alarm_on = True
    label_status.config(text=f"⏰ Báo thức {alarm_time}", fg="#005f99")
    if thread_bip and thread_bip.is_alive():
        dung_bip()

# --- Kiểm tra báo thức ---
def kiem_tra():
    global alarm_on, thread_bip
    while True:
        if alarm_on and time.strftime("%H:%M") == alarm_time:
            alarm_on = False
            label_status.config(text="🚨 Đến giờ báo thức!", fg="red")
            if not thread_bip or not thread_bip.is_alive():
                thread_bip = threading.Thread(target=phat_bip, daemon=True)
                thread_bip.start()
        time.sleep(1)

# --- Cập nhật giờ ---
def update_time():
    label_gio.config(text=time.strftime("%H:%M:%S"))
    root.after(1000, update_time)

# --- Giao diện ---
root = tk.Tk()
root.title("⏰ Đồng hồ báo thức")
root.geometry("420x360")
root.configure(bg="#e0f7fa")

tk.Label(root, text="⏰ Đồng hồ báo thức", font=("Arial", 20, "bold"), fg="#00796b", bg="#e0f7fa").pack(pady=10)
tk.Label(root, text="🕐 Giờ hiện tại:", font=("Arial", 14), bg="#e0f7fa").pack()

label_gio = tk.Label(root, text="", font=("Digital-7", 40, "bold"), fg="#00796b", bg="#e0f7fa")
label_gio.pack()
update_time()

tk.Label(root, text="👉 Nhấn A thử bíp (tăng dần)", font=("Arial", 11), bg="#e0f7fa").pack(pady=5)

tk.Label(root, text="Nhập giờ báo thức (HH:MM):", font=("Arial", 13), bg="#e0f7fa").pack(pady=5)
entry = tk.Entry(root, font=("Arial", 14), justify="center", width=10, relief="solid", bd=2)
entry.pack(pady=5)

frame = tk.Frame(root, bg="#e0f7fa")
frame.pack(pady=15)
tk.Button(frame, text="📅 Đặt báo thức", command=dat_bao_thuc, font=("Arial", 12), bg="#00796b", fg="white", width=15).grid(row=0, column=0, padx=10)
tk.Button(frame, text="🔕 Dừng báo thức", command=dung_bip, font=("Arial", 12), bg="#c62828", fg="white", width=15).grid(row=0, column=1, padx=10)

label_status = tk.Label(root, text="Chưa đặt báo thức", fg="gray", font=("Arial", 12), bg="#e0f7fa")
label_status.pack(pady=15)

# --- Luồng ---
threading.Thread(target=lang_nghe_phim, daemon=True).start()
threading.Thread(target=kiem_tra, daemon=True).start()

root.mainloop()
