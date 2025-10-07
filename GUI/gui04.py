import tkinter as tk

window = tk.Tk()
window.geometry("300x200")

font = "Arial"
size = 12

name_lbl = tk.Label(window, text="نام:", bg="lightblue", fg="black", font=("Arial", 14))
name_lbl.place(x=50, y=50, width=100, height=30)


name_entry = tk.Entry(window, bg="blue", fg="white", font=(font, size))
name_entry.place(x=80, y=60, width=150, height=25)

window.mainloop()
