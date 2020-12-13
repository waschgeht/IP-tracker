import functions as f
from sys import exit
from os import path


'''Main function thats gonna be startet by the schedules job!'''
def Main():
    Path = str(path.dirname(path.realpath(__file__)))
    ip = f.external_ip_requester() #Requests email from ifconfig.me/ip
    with open(Path + "\\data.conf", "r") as data: #Ließt Daten ein und ändert nur Eintrag 4 (Ip)
        ReadData = data.readlines()
        if str(ReadData[3]) == str(ip):
            exit()
        else:
            ReadData[3] = str(ip)

    with open(Path + "\\data.conf", "w") as Data: #Schreibt änderungen zum File
        Data.writelines(ReadData)
        Data.close()
    f.send_text()

Main()
