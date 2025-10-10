import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root)

# اضافه کردن فولدر اصلی
parent = tree.insert("", "end", text="Fruits")

# زیرشاخه‌ها
tree.insert(parent, "end", text="Apple")
tree.insert(parent, "end", text="Banana")
tree.insert(parent, "end", text="Orange")

tree.pack()
root.mainloop()
