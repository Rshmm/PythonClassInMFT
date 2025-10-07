import tkinter.messagebox as msg

answer = msg.askyesno("Confirm", "Do you want to delete this file?")
if answer:
    print("User chose YES")
else:
    print("User chose NO")
