import tkinter as tk

def on_release(event):
    print(f"ماوس رها شد در مختصات: ({event.x}, {event.y})")

window = tk.Tk()
btn = tk.Button(window, text="روی من کلیک کن")
btn.pack(padx=20, pady=20)

btn.bind("<ButtonRelease-1>", on_release)

window.mainloop()
