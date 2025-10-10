import tkinter as tk
from tkinter import ttk

def on_select(event):
    name_ent.delete(0, tk.END)
    age_ent.delete(0, tk.END)
    city_ent.delete(0, tk.END)
    selected_item = tree.focus()  # شناسه آیتم انتخاب‌شده
    values = tree.item(selected_item, "values")
    name_ent.insert(tk.END,values[0])
    age_ent.insert(tk.END,values[1])
    city_ent.insert(tk.END,values[2])

def add_too_list():
    name = name_ent.get()
    age = age_ent.get()
    city = city_ent.get()
    tree.insert("","end",values=(name,age,city))
    name_ent.delete(0,tk.END)
    age_ent.delete(0,tk.END)
    city_ent.delete(0,tk.END)


def edit_info():
    name = name_ent.get()
    age = age_ent.get()
    city = city_ent.get()
    tree.insert("", "end", values=(name, age, city))
    # selected_item = tree.focus()  # شناسه آیتم انتخاب‌شده
    # values = tree.item(selected_item, "values")
    # name_ent.insert(tk.END, values[0])
    # age_ent.insert(tk.END, values[1])
    # city_ent.insert(tk.END, values[2])


root = tk.Tk()
root.geometry("700x550")


tree = ttk.Treeview(root, columns=("name", "age", "city"), show="headings")
tree.heading("name", text="Name")
tree.heading("age", text="Age")
tree.heading("city", text="City")

# label
name_lbl = tk.Label(root,text="name").place(x=150, y=300)
age_lbl = tk.Label(root,text="age").place(x=150, y=350)
city_lbl = tk.Label(root,text="city").place(x=150, y=400)



# Entry
name_ent = tk.Entry(root)
name_ent.place(x=200, y=300)
age_ent = tk.Entry(root)
age_ent.place(x=200, y=350)
city_ent = tk.Entry(root)
city_ent.place(x=200, y=400)

# button
save_btn = tk.Button(root,text="save",command=add_too_list)
save_btn.place(x=200, y=450)
edit_btn = tk.Button(root,text="edit",command=edit_info)
edit_btn.place(x=250, y=450)

tree.bind("<<TreeviewSelect>>", on_select)
tree.pack(padx=10, pady=10)

root.mainloop()
