import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from controller import add_info_controller,remove_info_controller,edit_info_controller

def on_click(event):
    selected_item = table.focus()

    if not selected_item:
        return

    values = table.item(selected_item,"values")
    code_ent.delete(0, tk.END)
    name_ent.delete(0, tk.END)
    family_ent.delete(0, tk.END)
    age_ent.delete(0, tk.END)
    national_code_ent.delete(0, tk.END)
    code_ent.insert(0,values[0])
    name_ent.insert(0,values[1])
    family_ent.insert(0,values[2])
    age_ent.insert(0,values[3])
    national_code_ent.insert(0,values[4])



def save_click():
    code = code_ent.get()
    name = name_ent.get()
    family = family_ent.get()
    age = age_ent.get()
    national_code = national_code_ent.get()

    status, message = add_info_controller(code, name, family, age, national_code)
    if status:
        msg.showinfo("SAVED", message)
        table.insert("", "end", values=(code, name, family, age, national_code))
    else:
        msg.showerror("ERROR", message)

    code_ent.delete(0, tk.END)
    name_ent.delete(0, tk.END)
    family_ent.delete(0, tk.END)
    age_ent.delete(0, tk.END)
    national_code_ent.delete(0, tk.END)

def edit_click():
    selected_item = table.focus()
    if not selected_item:
        msg.showerror("Error", "Please select an item to edit")
        return


    new_name = name_ent.get()
    new_family = family_ent.get()
    new_age = age_ent.get()
    new_national_code = national_code_ent.get()

    # گرفتن مقدار قدیمی برای پیدا کردن در infos
    old_values = table.item(selected_item, "values")
    old_code = old_values[0]

    status, message = edit_info_controller(old_code, new_name, new_family, new_age, new_national_code)
    if status:
        msg.showinfo("EDITED", message)
        table.item(selected_item, values=(old_code, new_name, new_family, new_age, new_national_code))
    else:
        msg.showerror("ERROR", message)

    code_ent.delete(0, tk.END)
    name_ent.delete(0, tk.END)
    family_ent.delete(0, tk.END)
    age_ent.delete(0, tk.END)
    national_code_ent.delete(0, tk.END)

def remove_click():
    selected_item = table.focus()
    if not selected_item:
        msg.showerror("Error", "Please select an item to remove")
        return

    values = table.item(selected_item, "values")
    status, message = remove_info_controller(values[0])

    if status:
        msg.showinfo("REMOVED", message)
        table.delete(selected_item)
    else:
        msg.showerror("ERROR", message)

win = tk.Tk()

win.geometry("800x350")

# label
code_lbl = tk.Label(win, text="code")
code_lbl.place(x=20, y=20)
name_lbl = tk.Label(win, text="name")
name_lbl.place(x=20, y=60)
family_lbl = tk.Label(win, text="family")
family_lbl.place(x=20, y=100)
age_lbl = tk.Label(win, text="age")
age_lbl.place(x=20, y=140)
national_code_lbl = tk.Label(win, text="national code")
national_code_lbl.place(x=20, y=180)

# Entry

code = tk.StringVar()
name = tk.StringVar()
family = tk.StringVar()
age = tk.StringVar()
national_code = tk.StringVar()

code_ent = tk.Entry(win, textvariable=code)
code_ent.place(x=120, y=20)
name_ent = tk.Entry(win, textvariable=name)
name_ent.place(x=120, y=60)
family_ent = tk.Entry(win, textvariable=family)
family_ent.place(x=120, y=100)
age_ent = tk.Entry(win, textvariable=age)
age_ent.place(x=120, y=140)
national_code_ent = tk.Entry(win, textvariable=national_code)
national_code_ent.place(x=120, y=180)

# Button
save_btn = tk.Button(win, text="save", command=save_click)
save_btn.place(x=20, y=300, width=50)

edit_btn = tk.Button(win, text="edit", command=edit_click)
edit_btn.place(x=100, y=300, width=50)

remove_btn = tk.Button(win, text="remove", command=remove_click)
remove_btn.place(x=180, y=300, width=50)

# Table
table = ttk.Treeview(win, columns=(1, 2, 3, 4, 5), show="headings")
table.heading(1, text="code")
table.heading(2, text="name")
table.heading(3, text="family")
table.heading(4, text="age")
table.heading(5, text="national code")

table.column(1, width=90)
table.column(2, width=90)
table.column(3, width=90)
table.column(4, width=90)
table.column(5, width=90)

table.place(x=280, y=20)


table.bind("<<TreeviewSelect>>",on_click)

win.mainloop()
