import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg

goods = []

def save_click():
    code = code_ent.get()
    name = name_ent.get()
    brand = brand_ent.get()
    price = price_ent.get()

    for good in goods:
        if code == good['code']:
            msg.showerror("CODE","code already used")
            return


    goods.append({"code" : code, "name" : name, "brand" : brand, "price" : price})
    msg.showinfo("SAVED", "stuf saved successfully")

    table.insert("","end",values=(code,name,brand,price))

    code_ent.delete(0,tk.END)
    name_ent.delete(0,tk.END)
    brand_ent.delete(0,tk.END)
    price_ent.delete(0,tk.END)


def on_select(event):
    selected_item = table.focus()
    if not selected_item:
        return

    values = table.item(selected_item, "values")

    # پاک کردن فیلدها و پر کردن دوباره
    code_ent.delete(0, tk.END)
    name_ent.delete(0, tk.END)
    brand_ent.delete(0, tk.END)
    price_ent.delete(0, tk.END)

    code_ent.insert(0, values[0])
    name_ent.insert(0, values[1])
    brand_ent.insert(0, values[2])
    price_ent.insert(0, values[3])


def edit_click():
    selected_item = table.focus()
    if not selected_item:
        msg.showerror("Error", "Please select an item to edit")
        return

    code_new = code_ent.get()
    name_new = name_ent.get()
    brand_new = brand_ent.get()
    price_new = price_ent.get()

    # گرفتن مقدار قدیمی برای پیدا کردن در goods
    old_values = table.item(selected_item, "values")
    old_code = old_values[0]

    # آپدیت در لیست goods
    for good in goods:
        if good["code"] == old_code:
            good["code"] = code_new
            good["name"] = name_new
            good["brand"] = brand_new
            good["price"] = price_new
            break

    # آپدیت در جدول
    table.item(selected_item, values=(code_new, name_new, brand_new, price_new))

    msg.showinfo("Updated", "Item updated successfully!")

    # خالی کردن فیلدها
    code_ent.delete(0, tk.END)
    name_ent.delete(0, tk.END)
    brand_ent.delete(0, tk.END)
    price_ent.delete(0, tk.END)



def remove_click():
    selected_item = table.focus()
    if not selected_item:
        msg.showerror("Error", "Please select an item to remove")
        return

    # گرفتن مقادیر انتخاب‌شده
    values = table.item(selected_item, "values")
    code_to_remove = values[0]  # کد آیتمی که باید حذف شود

    # حذف از لیست goods
    for good in goods:
        if good["code"] == code_to_remove:
            goods.remove(good)
            break

    # حذف از جدول
    table.delete(selected_item)

    msg.showinfo("Removed", "Item removed successfully!")

    # خالی کردن فیلدها
    code_ent.delete(0, tk.END)
    name_ent.delete(0, tk.END)
    brand_ent.delete(0, tk.END)
    price_ent.delete(0, tk.END)


win = tk.Tk()

win.geometry("800x400")

code_lbl = tk.Label(win,text="code").place(x=30,y=40)
name_lbl = tk.Label(win,text="name").place(x=30,y=80)
brand_lbl = tk.Label(win,text="brand").place(x=30,y=120)
price_lbl = tk.Label(win,text="price").place(x=30,y=160)

code = tk.StringVar()
name = tk.StringVar()
brand = tk.StringVar()
price = tk.StringVar()

code_ent = tk.Entry(win,textvariable=code)
code_ent.place(x=100,y=40)
name_ent = tk.Entry(win,textvariable=name)
name_ent.place(x=100,y=80)
brand_ent = tk.Entry(win,textvariable=brand)
brand_ent.place(x=100,y=120)
price_ent = tk.Entry(win,textvariable=price)
price_ent.place(x=100,y=160)

save_btn = tk.Button(win,text="save", command=save_click)
save_btn.place(x=50, y=250, width=50)
edit_btn = tk.Button(win,text="edit", command=edit_click)
edit_btn.place(x=120, y=250,width=50)
edit_btn = tk.Button(win,text="remove", command=remove_click)
edit_btn.place(x=190, y=250,width=50)

table = ttk.Treeview(win,columns=(1,2,3,4),show="headings")
table.heading(1,text="code")
table.heading(2,text="name")
table.heading(3,text="brand")
table.heading(4,text="price")


table.column(1,width=60)
table.column(2,width=120)
table.column(3,width=120)
table.column(4,width=120)

table.place(x=300,y=40)

table.bind("<<TreeviewSelect>>", on_select)


win.mainloop()