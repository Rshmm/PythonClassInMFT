import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
from controller import save_person_controller, remove_person_controller, edit_person_controller, get_all_persons_controller

def update_table():
    for item in table.get_children():
        table.delete(item)
    persons = get_all_persons_controller()
    for person in persons:
        table.insert("", "end", values=person)


def on_table_select(event):
    selected_item = table.focus()
    if not selected_item:
        return
    person_data = table.item(selected_item,'values')
    code_ent.config(state="normal")
    code_ent.delete(0, tk.END)
    code_ent.insert(0, person_data[0])
    code_ent.config(state="disabled")
    name_ent.delete(0, tk.END)
    name_ent.insert(0, person_data[1])
    lastName_ent.delete(0, tk.END)
    lastName_ent.insert(0, person_data[2])
    age_ent.delete(0, tk.END)
    age_ent.insert(0, person_data[3])
    city_ent.delete(0, tk.END)
    city_ent.insert(0, person_data[4])
    addres_ent.delete(0, tk.END)
    addres_ent.insert(0, person_data[5])


def save_person():
    name = name_ent.get()
    lastName = lastName_ent.get()
    age = age_ent.get()
    city = city_ent.get()
    addres = addres_ent.get()
    success, message = save_person_controller(name,lastName,age,city,addres)
    if success:
        messagebox.showinfo("Success", message)
        update_table()
    else:
        messagebox.showerror("Error", message)
    code_ent.config(state="normal")
    code_ent.delete(0, tk.END)
    code_ent.config(state="disabled")
    name_ent.delete(0, tk.END)
    lastName_ent.delete(0, tk.END)
    age_ent.delete(0, tk.END)
    city_ent.delete(0, tk.END)
    addres_ent.delete(0, tk.END)


def remove_person():
    person_code = code_ent.get()
    success, message = remove_person_controller(person_code)
    if success:
        messagebox.showinfo("Success", message)
        update_table()
    else:
        messagebox.showerror("Error", message)


def edit_person():
    person_code = code_ent.get()
    name = name_ent.get()
    lastName = lastName_ent.get()
    age = age_ent.get()
    city = city_ent.get()
    addres = addres_ent.get()
    success, message = edit_person_controller(person_code,name,lastName,age,city,addres)
    if success:
        messagebox.showinfo("Success", message)
        update_table()
    else:
        messagebox.showerror("Error", message)


win = tk.Tk()

win.geometry("1000x500")

win.title("Person Online Shop")

main_frame = tk.Frame(win)
search_frame = tk.Frame(win)

for frame in (main_frame, search_frame):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

def show_frame(frame):
    frame.tkraise()

code_label = ttk.Label(main_frame, text="Code:")
code_label.config(state="disabled")
code_label.place(x=40,y=50,width=200,height=30)
name_label = ttk.Label(main_frame, text="name:")
name_label.place(x=40,y=100,width=200,height=30)
lastName_label = ttk.Label(main_frame, text="last name:")
lastName_label.place(x=40,y=150,width=200,height=30)
age_label = ttk.Label(main_frame, text="age:")
age_label.place(x=40,y=200,width=200,height=30)
city_label = ttk.Label(main_frame, text="city:")
city_label.place(x=40,y=250,width=200,height=30)
addres_label = ttk.Label(main_frame,text="address:")
addres_label.place(x=40,y=300,width=200,height=30)

code_ent = ttk.Entry(main_frame)
code_ent.config(state="disabled")
code_ent.place(x=150,y=50,width=200,height=30)
name_ent = ttk.Entry(main_frame)
name_ent.place(x=150,y=100,width=200,height=30)
lastName_ent = ttk.Entry(main_frame)
lastName_ent.place(x=150,y=150,width=200,height=30)
age_ent = ttk.Entry(main_frame)
age_ent.place(x=150,y=200,width=200,height=30)
city_ent = ttk.Entry(main_frame)
city_ent.place(x=150,y=250,width=200,height=30)
addres_ent = ttk.Entry(main_frame)
addres_ent.place(x=150,y=300,width=200,height=30)


table = ttk.Treeview(main_frame, columns=("code","name", "lastName", "age", "city", "address"), show="headings")

table.heading("code", text="Code")
table.heading("name", text="Name")
table.heading("lastName", text="Last Name")
table.heading("age", text="Age")
table.heading("city", text="City")
table.heading("address", text="Address")


table.column("code", width=50)
table.column("name", width=100) 
table.column("lastName", width=100)
table.column("age", width=50)
table.column("city", width=100)
table.column("address", width=150)

 
table.place(x=400, y=50, height=300)

update_table()

table.bind("<<TreeviewSelect>>", on_table_select)

save_btn = ttk.Button(main_frame, text="Save Person", command=save_person)
save_btn.place(x=50, y=400)
remove_btn = ttk.Button(main_frame, text="Remove Person", command=remove_person)
remove_btn.place(x=150, y=400)
edit_btn = ttk.Button(main_frame, text="Edit Person", command=edit_person)
edit_btn.place(x=250, y=400)

search_btn = ttk.Button(main_frame,text="Search",command=lambda: show_frame(search_frame))
search_btn.place(x=350, y=400)



back = ttk.Button(search_frame,text="Back",command=lambda: show_frame(main_frame))
back.place(x=10, y=450)

show_frame(main_frame)

win.mainloop()