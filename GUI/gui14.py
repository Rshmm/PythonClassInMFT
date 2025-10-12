import tkinter as tk
import tkinter.ttk as ttk



win = tk.Tk()

def show_info():
    print("code : " , type(code.get()))
    print("code : " , type(name.get()))
    print("code : " , type(brand.get()))
    print("code : " , type(price.get()))

code = tk.IntVar()
name = tk.StringVar()
brand = tk.StringVar()
price = tk.IntVar()


code_lbl = tk.Label(win,text="code").pack()
name_lbl = ttk.Label(win,text="name").pack()
brand_lbl = tk.Label(win,text="brand").pack()
price_lbl = tk.Label(win,text="price").pack()


ttk.Frame(win)

code_ent = ttk.Entry(win,textvariable=code).pack()
name_ent = tk.Entry(win,textvariable=name).pack()
brand_ent = tk.Entry(win,textvariable=brand).pack()
price_ent = tk.Entry(win,textvariable=price).pack()


show_info_btn = ttk.Button(win,text="show", command=show_info).pack()

win.mainloop()