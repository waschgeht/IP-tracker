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

try:
    root = tk.Tk()
    tk.Label(root, text="First Name").grid(row=0)
    tk.Label(root, text="Last Name").grid(row=1)
    e1 = tk.Entry(root)
    e2 = tk.Entry(root)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    root.mainloop()
except:
    root.destroy()