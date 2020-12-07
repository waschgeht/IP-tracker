import tkinter as tk
import functions as f


try:
    root = tk.Tk()
    tk.Label(root, text="Please be aware, for this to work you need to \n enable less safer apps on gmail!\n To do so please follow this link: \n \n https://myaccount.google.com/lesssecureapps \n").pack()
    tk.Button(root, text="Ok", command=root.destroy).pack()
    root.mainloop()
except:
    root.destroy()
    f.logging("Startwindow failure")

