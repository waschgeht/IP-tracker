from os import popen, path
from smtplib import SMTP_SSL
from _datetime import datetime
from base64 import b64encode, b64decode
'''funktion requestet ip von ifconfig.me'''
def external_ip_requester():
    try:
        ip = str(popen("curl http://ifconfig.me/ip").read()) #.popen erzeugt keine Ausgabe am Screen
        int(ip[0]) #testet ob ausgabe eine IP ist. Erzeugt fehler wenn falsch und läuft in except block
        return ip
    except:
        print("Couldnt get ip from http://ifconfig.me/ip")
        raise SystemExit(0) #schließt das programm komplett


'''Base 64 encodes and decodes messages'''
def bencode(secret):
    return b64encode(bytes(secret, encoding='utf-8')).decode('ascii')

def bdecode(secret):
    return b64decode(secret).decode('ascii')



'''
Sendet plain text message
'''
def send_text():
    Path = str(path.dirname(path.realpath(__file__)))
    with open(Path + "\\data.conf", "r") as data: #liest daten aus .conf file; Positionsabhängig!!!
        Data = data.readlines()
        for i in range(0,3):
            print(Data[i])
            Data[i] = bdecode(Data[i])
            print(Data[i])
    try:
        message = 'Subject: {}\n\n{}'.format("Your current IP", "Your current IP is " + Data[3]) #erstellt message mit Data[2]=IP
        server = SMTP_SSL("smtp.gmail.com", 465) #funktionierrt nur für gmail server. Applikationszugriff uss aktiviert sein
        server.login(Data[0], Data[1])  #Data[0]=your email; Data[1]=your Email password
        server.sendmail(Data[0], Data[2], message) #Data[0]=your email; Data[2]=receiver email
        server.quit()
        logging("Email was sent")
    except Exception as error:
        print("Error, couldn't send message")
        print(error)
        logging("Couldn't send email;   " + str(error))


def logging(TEXT):
    Path = str(path.dirname(path.realpath(__file__)))
    file_location = Path + "\\email.log"
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with open(file_location, "a+") as log:
            log.write(date + ";   " + TEXT + " \n")
    except Exception as nopen1:
        print("Couldn't write to file")
        print(nopen1)

def schedule_task(frequency, time):
    Path = str(path.dirname(path.realpath(__file__)))
    if popen('SCHTASKS | findstr /b ip_tracker').read()=="":
        try:
            popen('SCHTASKS /CREATE /SC ' + str(frequency) + ' /TN "ip_tracker" /TR "' + Path + '\\main.py" /ST ' + str(time))
            logging("Task wurde erstellt")
        except Exception as error:
            logging("Fehler beim erstellen von Task; ", error)
    else:
        try:
            popen('SCHTASKS /DELETE /TN "ip_tracker" /f')
            popen('SCHTASKS /CREATE /SC ' + str(frequency) + ' /TN "ip_tracker" /TR  "' + Path + '\\main.py" /ST ' + str(time))
            logging("Task wurde erstellt")
        except Exception as error:
            logging("Fehler beim erstellen von Task; ", error)

def  disable_task():
    try:
        popen('SCHTASKS /CHANGE /TN "ip_tracker" /DISABLE')
        logging("Task disabled")
    except Exception as error:
        logging("Couldn't disable task; ", error)

def enable_task():
    try:
        popen('SCHTASKS /CHANGE /TN "ip_tracker" /ENABLE')
        logging("Task enabled")
    except Exception as error:
        logging("Couldn't enable task; ", error)


def WriteToFile(email, password, receiver, ip):
    Path = str(path.dirname(path.realpath(__file__)))
    with open(Path + "\\data.conf", "w+") as file:
        file.writelines([email, "\n", password, "\n", receiver, "\n", ip])


