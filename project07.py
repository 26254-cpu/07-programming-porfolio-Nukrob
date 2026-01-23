import tkinter as tk
from tkinter import messagebox

# นายนักรบ ปริพินิจฉัย เลขที่ 7 ม.4/4

def calculate():
    try:
        # รับค่าจากช่องกรอกข้อมูล (Entry widgets)
        username = entry_name.get()
        money_str = entry_money.get()
        percent_str = entry_percent.get()

        # ตรวจสอบว่ามีการกรอกข้อมูลครบหรือไม่
        if not username or not money_str or not percent_str:
            messagebox.showwarning("ข้อมูลไม่ครบ", "กรุณากรอกข้อมูลให้ครบทุกช่องครับ")
            return

        # แปลงค่าตัวเลข
        money = int(money_str)
        percentage = float(percent_str)

        # --- ส่วนการประมวลผล (Process) เหมือนเดิม ---
        total_allowed_spending_for_5_days = money * (percentage / 100)
        daily_spending_limit = total_allowed_spending_for_5_days / 5
        remaining_money = money - total_allowed_spending_for_5_days
        remaining_percentage = (remaining_money / money) * 100

        # เตรียมข้อความผลลัพธ์
        result_text = (
            f"--------------------------------------------------\n"
            f"คุณ {username} ควรใช้จ่ายไม่เกิน {daily_spending_limit:.2f} บาทต่อวัน\n"
            f"เพื่อให้เป็นไปตาม {percentage:.2f}% ของเงินทั้งหมด {money} บาท\n"
            f"--------------------------------------------------\n"
            f"ถ้าผู้ใช้ ใช้จ่ายตามจำนวนเงินที่ระบุไว้ ยอดเงินจะเหลือเท่าไหร่: {remaining_money:.2f} บาท\n"
            f"สามารถตีเป็นเปอร์เซ็นต์คงเหลือได้: {remaining_percentage:.2f}%\n"
            f"หากคุณใช้จ่ายตามจำนวนที่ทางเราแนะนำ ยอดใช้จ่ายที่คุณใช้ไปคือ: {total_allowed_spending_for_5_days:.2f} บาท/THB\n"
            f"ซึ่งสามารถตีเป็นค่าร้อยละของยอดใช้จ่ายได้ คือ: {percentage:.2f}%"
        )

        # แสดงผลลัพธ์ที่ Label ด้านล่าง
        lbl_result.config(text=result_text, fg="blue")

    except ValueError:
        messagebox.showerror("ข้อมูลผิดพลาด", "กรุณากรอก จำนวนเงิน และ เปอร์เซ็นต์ เป็นตัวเลขเท่านั้น")

# --- การสร้างหน้าต่าง GUI ---
root = tk.Tk()
root.title("โปรแกรมคำนวณการออม - นายนักรบ ปริพินิจฉัย")
root.geometry("500x550") # กำหนดขนาดหน้าต่างกว้าง x สูง

# ส่วนหัวข้อ
lbl_header = tk.Label(root, text="ระบบคำนวณวางแผนการใช้เงิน 5 วัน", font=("Arial", 16, "bold"))
lbl_header.pack(pady=10)

# 1. รับชื่อ
frame_name = tk.Frame(root)
frame_name.pack(pady=5)
tk.Label(frame_name, text="ชื่อของคุณ:", font=("Arial", 12)).pack(side=tk.LEFT)
entry_name = tk.Entry(frame_name, font=("Arial", 12))
entry_name.pack(side=tk.LEFT, padx=10)

# 2. รับจำนวนเงิน
frame_money = tk.Frame(root)
frame_money.pack(pady=5)
tk.Label(frame_money, text="จำนวนเงินรวม 5 วัน:", font=("Arial", 12)).pack(side=tk.LEFT)
entry_money = tk.Entry(frame_money, font=("Arial", 12))
entry_money.pack(side=tk.LEFT, padx=10)

# 3. รับเปอร์เซ็นต์
frame_percent = tk.Frame(root)
frame_percent.pack(pady=5)
tk.Label(frame_percent, text="เปอร์เซ็นต์ที่ต้องการใช้:", font=("Arial", 12)).pack(side=tk.LEFT)
entry_percent = tk.Entry(frame_percent, font=("Arial", 12))
entry_percent.pack(side=tk.LEFT, padx=10)

# ปุ่มคำนวณ
btn_calc = tk.Button(root, text="คำนวณผลลัพธ์", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=calculate)
btn_calc.pack(pady=20)

# พื้นที่แสดงผลลัพธ์
lbl_result = tk.Label(root, text="ผลลัพธ์จะแสดงที่นี่...", font=("Arial", 11), justify=tk.LEFT, bg="#f0f0f0", padx=10, pady=10)
lbl_result.pack(pady=10, fill=tk.BOTH, expand=True)

# เริ่มต้นโปรแกรม
root.mainloop()
