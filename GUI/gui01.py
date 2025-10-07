import tkinter as tk
import tkinter.messagebox as msg


names = []

def add_name():
    name = name_ent.get()
    family = family_ent.get()

    names.append({"name" : name, "family": family})
    for item in names:
        print(f"name: {item['name']}, family: {item['family']}")

    print("*" * 50)

    msg.showinfo("Save", "person name saved successfully")

    name_ent.delete(0, tk.END)
    family_ent.delete(0, tk.END)



win = tk.Tk()

win.title("online shop")

win.geometry("800x500")

name_lbl = tk.Label(win,text="Name")
name_lbl.place(x=50,y=50)

family_lbl = tk.Label(win,text="Family")
family_lbl.place(x=50,y=100)


name_ent = tk.Entry(win)
name_ent.place(x=100,y=50)

family_ent = tk.Entry(win)
family_ent.place(x=100,y=100)

save_btn = tk.Button(win,text="Save", command=add_name)
save_btn.place(x= 100, y=400,width=70)

edit_btn = tk.Button(win,text="edit")
edit_btn.place(x= 250, y=400,width=70)

remove_btn = tk.Button(win,text="remove")
remove_btn.place(x= 400, y=400,width=70)

win.mainloop()