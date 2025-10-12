import tkinter as tk

win = tk.Tk()
win.title("فرم محصول")

code = tk.IntVar()
name = tk.StringVar()
brand = tk.StringVar()
price = tk.IntVar()

tk.Label(win, text="کد:").grid(row=0, column=0)
tk.Label(win, text="نام:").grid(row=1, column=0)
tk.Label(win, text="برند:").grid(row=2, column=0)
tk.Label(win, text="قیمت:").grid(row=3, column=0)

code_ent = tk.Entry(win, textvariable=code)
name_ent = tk.Entry(win, textvariable=name)
brand_ent = tk.Entry(win, textvariable=brand)
price_ent = tk.Entry(win, textvariable=price)

code_ent.grid(row=0, column=1)
name_ent.grid(row=1, column=1)
brand_ent.grid(row=2, column=1)
price_ent.grid(row=3, column=1)

def show_info():
    print("کد:", type(code.get()))
    print("نام:", type(name.get()))
    print("برند:", type(brand.get()))
    print("قیمت:", type(price.get()))

btn = tk.Button(win, text="نمایش اطلاعات", command=show_info)
btn.grid(row=4, column=0, columnspan=2, pady=10)

win.mainloop()
