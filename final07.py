import tkinter as tk
from tkinter import messagebox
import datetime

def calculate_age():
    try:
        # ดึงปีปัจจุบัน พ.ศ.
        buddhist_current_year = datetime.datetime.now().year + 543
        
        # รับค่าจากช่องกรอก
        birth_year = int(entry_year.get())
        
        # คำนวณอายุ
        age = buddhist_current_year - birth_year
        
        if age < 0:
            messagebox.showwarning("ข้อผิดพลาด", "ปีเกิดห้ามมากกว่าปีปัจจุบันนะ!")
        else:
            label_result.config(text=f"ปีปัจจุบัน (พ.ศ.): {buddhist_current_year}\nคุณมีอายุประมาณ: {age} ปี", fg="#2ecc71")
            
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกเฉพาะตัวเลขปี พ.ศ. เท่านั้น")

# --- สร้างหน้าต่างหลัก ---
root = tk.Tk()
root.title("นายนักรบ ปริพินิจฉัย เลขที่ 7 ม.4/4")
root.geometry("400x300")
root.configure(bg="#f0f3f5")

# ส่วนหัวข้อ (Title)
header = tk.Label(root, text="โปรแกรมคำนวณอายุ", font=("Arial", 18, "bold"), bg="#f0f3f5", fg="#34495e")
header.pack(pady=20)

# ช่องกรอกข้อมูล
tk.Label(root, text="กรุณากรอกปีเกิด (พ.ศ.):", font=("Arial", 12), bg="#f0f3f5").pack()
entry_year = tk.Entry(root, font=("Arial", 14), justify='center')
entry_year.pack(pady=10)

# ปุ่มคำนวณ
btn_calculate = tk.Button(root, text="คำนวณอายุ", command=calculate_age, font=("Arial", 12, "bold"), 
                          bg="#3498db", fg="white", padx=20, pady=5, cursor="hand2")
btn_calculate.pack(pady=10)

# ส่วนแสดงผลลัพธ์
label_result = tk.Label(root, text="", font=("Arial", 13, "bold"), bg="#f0f3f5")
label_result.pack(pady=10)

# รันโปรแกรม
root.mainloop()
