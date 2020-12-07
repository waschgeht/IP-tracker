import tkinter as tk
#import waschgeht.functions as f


try:
    root = tk.Tk()
    tk.Label(root, text="Please be aware, for this to work you need to \n enable less safer apps on gmail!\n To do so please follow this link: \n \n https://myaccount.google.com/lesssecureapps \n").pack()
    tk.Button(root, text="Ok", command=root.destroy).pack()
    root.mainloop()
except:
    root.destroy()
 #   f.logging("Startwindow failure")


'''Gui buit up with grid'''
try:
    root = tk.Tk()
    root.title("IP tracker") #titel
    tk.Label(root, text="Your Email").grid(row=0) #Label with Grid
    tk.Label(root, text="Your Password").grid(row=1)
    tk.Label(root, text="Receiver Email").grid(row=0, column=3)
    tk.Label(root, text="Frequency").grid(row=2)
    tk.Label(root, text="Enable/Disable").grid(row=2, column=3)

    e1 = tk.Entry(root) #Eingabefelder Email
    e2 = tk.Entry(root) #Enter password
    e3 = tk.Entry(root) #Enter receiver
    e1.grid(row=0, column=1, padx=10, pady=10) #Padding applies to both sides x for x axis y for y axis
    e2.grid(row=1, column=1, padx=10, pady=10)
    e3.grid(row=0, column=4,padx=10, pady=10)

    frequence = tk.StringVar(root) #Variable for drop down menue
    frequence.set("hourly")  # default value
    w = tk.OptionMenu(root, frequence, "hourly", "dayly", "weekly") #Dropdown choices
    w.grid(row=3, column=0,padx=10)

    variableEn = tk.StringVar(root) #Variable for drop down menue
    variableEn.set("enable")  # default value
    Enabler = tk.OptionMenu(root, variableEn, "enable", "disable")  # Dropdown choices
    Enabler.grid(row=3, column=3, padx=10)
    root.mainloop()
except:
    root.destroy()