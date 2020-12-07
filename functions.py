import os
import smtplib
from _datetime import datetime

'''funktion requestet ip von ifconfig.me'''
def external_ip_requester():
    try:
        ip = str(os.popen("curl http://ifconfig.me/ip").read()) #.popen erzeugt keine Ausgabe am Screen
        int(ip[0]) #testet ob ausgabe eine IP ist. Erzeugt fehler wenn falsch und läuft in except block
        return ip
    except:
        print("Couldnt get ip from http://ifconfig.me/ip")
        raise SystemExit(0) #schließt das programm komplett


'''
Sendet plain text message
'''
def send_text():
    with open("data.conf", "r") as data: #liest daten aus .conf file; Positionsabhängig!!!
        Data = data.readlines()
    try:
        message = 'Subject: {}\n\n{}'.format("Your current IP", "Your current IP is " + Data[2]) #erstellt message mit Data[2]=IP
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465) #funktionierrt nur für gmail server. Applikationszugriff uss aktiviert sein
        server.login(Data[0], Data[1])  #Data[0]=your email; Data[1]=your Email password
        server.sendmail(Data[0], Data[3], message) #Data[0]=your email; Data[3]=receiver email
        server.quit()
        logging("Email was sent")
    except Exception as error:
        print("Error, couldn't send message")
        print(error)
        logging("Couldn't send email;   " + str(error))


def logging(TEXT):
    folder_loacation = os.getcwd()
    file_location = folder_loacation + "\\email.log"
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with open(file_location, "a+") as log:
            log.write(date + ";   " + TEXT + " \n")
    except Exception as nopen1:
        print("Couldn't write to file")
        print(nopen1)

def schedule_task(frequency, time):
    if os.popen('SCHTASKS | findstr /b ip_tracker').read()=="":
        try:
            os.popen('SCHTASKS /CREATE /SC ' + frequency + ' /TN "ip_tracker" /TR "C:\Users\waschgeht\ip_tracker\main.py" /ST ' + str(time))
            logging("Task wurde erstellt")
        except Exception as error:
            logging("Fehler beim erstellen von Task; ", error)
    else:
        try:
            os.popen('SCHTASKS /CHANGE /SC ' + frequency + ' /TN "ip_tracker" /ST ' + str(time))
            logging("Task wurde erstellt")
        except Exception as error:
            logging("Fehler beim erstellen von Task; ", error)

def  disable_task():
    try:
        os.popen('SCHTASKS /CHANGE /TN "ip_tracker" /DISABLE')
        logging("Task disabled")
    except Exception as error:
        logging("Couldn't disable task; ", error)

def enable_task():
    try:
        os.popen('SCHTASKS /CHANGE /TN "ip_tracker" /ENABLE')
        logging("Task enabled")
    except Exception as error:
        logging("Couldn't enable task; ", error)

def generate_gui():
