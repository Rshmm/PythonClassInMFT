import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview Example")

# ایجاد ویجت Treeview
tree = ttk.Treeview(root)

# تعریف ستون‌ها
tree["columns"] = ("name", "age", "city")

# تنظیم اندازه و عنوان ستون‌ها
tree.column("#0", width=100, minwidth=50)  # ستون درخت (اصلی)
tree.column("name", width=120)
tree.column("age", width=50)
tree.column("city", width=100)

# عنوان هر ستون
tree.heading("#0", text="ID")
tree.heading("name", text="Name")
tree.heading("age", text="Age")
tree.heading("city", text="City")

# اضافه کردن داده‌ها
tree.insert("", "end", iid=1, text="1", values=("Ali", 25, "Tehran"))
tree.insert("", "end", iid=2, text="2", values=("Sara", 30, "Shiraz"))
tree.insert("", "end", iid=3, text="3", values=("Arsham", 27, "Bushehr"))

tree.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()
