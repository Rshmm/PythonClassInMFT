import tkinter as tk

def say_hello():
    label.config(text="سلام دوباره!")

window = tk.Tk()
window.title("Button Example")

label = tk.Label(window, text="روی دکمه کلیک کن!", font=("Arial", 14))
label.pack(pady=10)

button = tk.Button(window, text="کلیک کن", command=say_hello)
button.pack(pady=10)

window.mainloop()
