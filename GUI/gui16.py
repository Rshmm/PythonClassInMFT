import tkinter as tk

def search_win():
    search_win = tk.Tk()

    search_win.geometry("400x500")

    search_win.mainloop()


win = tk.Tk()

win.geometry("400x500")


search_btn = tk.Button(text = "search", command=search_win)
search_btn.place(x=50,y=50)



win.mainloop()