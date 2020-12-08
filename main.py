import ip_tracker.functions as f
import sys

'''Main function thats gonna be Starteet by the Schedules Job!'''
def Main():
    ip = f.external_ip_requester() #Requests email from ifconfig.me/ip
    with open("data.conf", "r") as data: #Ließt Daten ein und ändert nur Eintrag 4 (Ip)
        ReadData = data.readlines()
        if str(ReadData[3]) == str(ip):
            sys.exit()
        else:
            ReadData[3] = str(ip)

    with open("data.conf", "w") as Data: #Schreibt änderungen zum File
        Data.writelines(ReadData)
        Data.close()
    f.send_text()


Main()