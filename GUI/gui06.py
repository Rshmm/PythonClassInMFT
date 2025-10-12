import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Treeview Example")

win.geometry("450x450")

# ایجاد ویجت Treeview
tree = ttk.Treeview(win,columns=(1,2,3),show="headings")

tree.column(1,width=120)
tree.column(2,width=50)
tree.column(3,width=100)

# عنوان هر ستون
tree.heading(1,text="Name")
tree.heading(2,text="Age")
tree.heading(3,text="City")

# اضافه کردن داده‌ها
tree.insert("", "end", values=("Ali", 25, "Tehran"))
tree.insert("", "end", values=("Sara", 30, "Shiraz"))
tree.insert("", "end", values=("Arsham", 27, "Bushehr"))

tree.place(x=20,y=20)

win.mainloop()
