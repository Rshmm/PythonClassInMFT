import tkinter as tk

def show_name():
    name = name_entry.get()
    label.configure(text=f"Hello {name}!")

window = tk.Tk()
window.geometry("300x200")

font = "Arial"
size = 12

name_entry = tk.Entry(window, bg="white", fg="black", font=(font, size))
name_entry.place(x=80, y=50, width=150, height=25)

btn = tk.Button(window, text="GO", bg="lightblue", fg="black", font=(font, size), command=show_name)
btn.place(x=100, y=90, width=100, height=30)

label = tk.Label(window, text="", font=(font, size))
label.place(x=80, y=130)

window.mainloop()


import tkinter as tk
from tkinter import messagebox  # 👈 اینو اضافه می‌کنیم

def show_name():
    name = name_entry.get()
    # پیام رو در messagebox نمایش می‌دیم
    messagebox.showinfo("Greeting", f"Hello {name}!")  # 👈 این خط

window = tk.Tk()
window.geometry("300x200")

font = "Arial"
size = 12

name_entry = tk.Entry(window, bg="white", fg="black", font=(font, size))
name_entry.place(x=80, y=50, width=150, height=25)

btn = tk.Button(window, text="GO", bg="lightblue", fg="black", font=(font, size), command=show_name)
btn.place(x=100, y=90, width=100, height=30)

window.mainloop()