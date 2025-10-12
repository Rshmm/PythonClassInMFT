import tkinter as tk

def on_key(event):
    print("کلید فشرده شد:", event.char)

window = tk.Tk()
window.bind("<Key>", on_key)  # روی کل پنجره گوش می‌ده
window.mainloop()
