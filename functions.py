import os
import smtplib
from _datetime import datetime
from email.message import EmailMessage

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
    with open(data.conf, "r") as data:
        Data = data.readline()
    try:
        message = 'Subject: {}\n\n{}'.format("Your current IP", "Your current IP is " + Data[2])
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(Data[0], Data[1])
        server.sendmail(Data[0], Data[3], message)
        server.quit()
    except Exception as error:
        print("Error, couldn't send message")
        print(error)
        logging("Couldn't send email")


def logging(TEXT):
    folder_loacation = os.getcwd()
    file_location = folder_loacation + "\\email.log"
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with open(file_location, "a+") as log:
            log.write(date + ";   " + TEXT  + " \n")
    except Exception as nopen1:
        print("Couldn't write to file")
        print(nopen1)
