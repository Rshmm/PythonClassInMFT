import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_item = tree.focus()  # شناسه آیتم انتخاب‌شده
    values = tree.item(selected_item, "values")
    print("Selected:", values)

root = tk.Tk()

tree = ttk.Treeview(root, columns=("name", "age", "city"), show="headings")
tree.heading("name", text="Name")
tree.heading("age", text="Age")
tree.heading("city", text="City")

data = [
    ("Ali", 25, "Tehran"),
    ("Sara", 30, "Shiraz"),
    ("Arsham", 27, "Bushehr")
]

for item in data:
    tree.insert("", "end", values=item)

tree.bind("<<TreeviewSelect>>", on_select)
tree.pack(padx=10, pady=10)

root.mainloop()
