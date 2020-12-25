import tkinter as tk
import functions as f
from urllib.request import urlretrieve
from tkinter import ttk
import time

def CancelButton():
    root.destroy()

def ApplyButton():
    if EnableDiable.get()=="disable":
        f.disable_task()
    elif EnableDiable.get()=="enable":
        f.WriteToFile(f.bencode(e1.get()),f.bencode(e2.get()), f.bencode(e3.get()), f.external_ip_requester())
        f.schedule_task(frequence.get(), e4.get())
        f.send_text()
    root.destroy()

def bar_update(bar, Wert):
    bar['value'] = Wert
    root.update_idletasks()
    time.sleep(1)

def download():
    bar = ttk.Progressbar(root, orient="horizontal", length=200)
    bar.grid(row=2, columnspan=2, padx=30, pady=20)
    bar_update(bar, 0)
    urlretrieve("http://softwareupdt.duckdns.org:8080/ip_tracker/gui.py", "gui.py")
    bar_update(bar, 33)
    urlretrieve("http://softwareupdt.duckdns.org:8080/ip_tracker/functions.py", "functions.py")
    bar_update(bar, 66)
    urlretrieve("http://softwareupdt.duckdns.org:8080/ip_tracker/main.py", "main.py")
    bar_update(bar, 100)
    root.destroy()

try:
    root = tk.Tk()
    photo = tk.PhotoImage(file=f.Pfad() + "\\icon1.png")
    root.iconphoto(False, photo)
    root.title("IP tracker")  # titel
    tk.Label(root, text="Please be aware, for this to work you need to \n enable less safer apps on gmail!\n To do so please follow this link: \n \n https://myaccount.google.com/lesssecureapps \n").pack()
    tk.Button(root, text="Ok", command=root.destroy).pack()
    root.mainloop()
except:
    root.destroy()
    f.logging("Startwindow failure")

try:
    if f.new_update():
        try:
            root = tk.Tk()
            photo = tk.PhotoImage(file=f.Pfad() + "\\icon1.png")
            root.iconphoto(False, photo)
            root.title("Update available!")  # titel
            tk.Label(root, text="There is a new update available, \n do you want to download the newest version?").grid(row=0, columnspan=2, padx=10, pady=10)
            tk.Button(root, text="   Yes   ", command=download).grid(row=1, column=0,padx=10, pady=10, sticky=tk.E)
            tk.Button(root, text="   No   ", command=root.destroy).grid(row=1, column=1,padx=10, pady=10, sticky=tk.W)
            tk.Label(root, text="     ").grid(row=2, columnspan=2, padx=30, pady=20)
            root.mainloop()
        except:
            root.destroy()
            f.logging("Updatewindow failure")
except:
    f.logging("Update failure")

'''Gui buit up with grid'''
try:
    global e1, e2, e3
    root = tk.Tk()
    photo = tk.PhotoImage(file=f.Pfad() + "\\icon1.png")
    root.iconphoto(False, photo)
    root.title("IP tracker") #titel
    tk.Label(root, text="Your Email").grid(row=0) #Label with Grid
    tk.Label(root, text="Your Password").grid(row=1)
    tk.Label(root, text="Receiver Email").grid(row=0, column=3)
    tk.Label(root, text="Frequency").grid(row=2, pady=(30,0))
    tk.Label(root, text="Enable/Disable").grid(row=2, column=4, pady=(30,0))
    tk.Label(root, text="Starttime").grid(row=2, column=1, pady=(30,0), sticky=tk.W)

    e1 = tk.Entry(root, width=40) #Eingabefelder Email
    e2 = tk.Entry(root, show="*", width=40) #Enter password
    e3 = tk.Entry(root, width=40) #Enter receiver
    e4 = tk.Entry(root)  # Enter Starttime (Format 17:30)

    e1.grid(row=0, column=1, padx=10, pady=10) #Padding applies to both sides x for x axis y for y axis
    e2.grid(row=1, column=1, padx=10, pady=10)
    e3.grid(row=0, column=4,padx=10, pady=10)
    e4.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

    frequence = tk.StringVar(root) #Variable for drop down menue
    frequence.set("hourly")  # default value
    w = tk.OptionMenu(root, frequence, "hourly", "dayly").grid(row=3, column=0,padx=10) #Dropdown choices for frequency of Task Scheduler

    EnableDiable = tk.StringVar(root) #Variable for drop down menue
    EnableDiable.set("enable")  # default value
    Enabler = tk.OptionMenu(root, EnableDiable, "enable", "disable")  # Dropdown choices
    Enabler.grid(row=3, column=4, padx=10)

    '''This function toggles the entry widgets away is the ip_tracker should be disabled'''
    def toogle(*args):
        global e1,e2, e3
        if EnableDiable.get() == "disable":
            e1.grid_forget()
            e2.grid_forget()
            e3.grid_forget()
            e4.grid_forget()
        elif EnableDiable.get() == "enable":
            e1.grid(row=0, column=1, padx=10, pady=10)  # Padding applies to both sides x for x axis y for y axis
            e2.grid(row=1, column=1, padx=10, pady=10)
            e3.grid(row=0, column=4, padx=10, pady=10)
            e4.grid(row=3, column=1, padx=10, pady=10)
    EnableDiable.trace("w", toogle) #Tracks changes in the EnableDisable variable and calls the toggle function if so
    '''Set Button, that Sets all the values from the widget'''
    tk.Button(root, text="Apply Settings", command=ApplyButton).grid(row=4, column=3, padx=5, pady=(100,5))
    '''Cancel Button destroys the gui'''
    tk.Button(root, text="Cancel", command=CancelButton).grid(row=4, column=4, padx=5, pady=(100,5))
    root.mainloop()
except Exception as error:
    root.destroy()
    f.logging("Gui failed; " + str(error))