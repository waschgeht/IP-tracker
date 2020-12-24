from os import path
from smtplib import SMTP_SSL
from _datetime import datetime
from base64 import b64encode, b64decode
from subprocess import Popen, PIPE




'''umgehe noconsole error bei convert durch pyinstaller'''
def cmd(command):
    process = Popen(command, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    ip = process.communicate()
    return ip

def new_update():
    try:
        newest_version = float(cmd("curl -s http://softwareupdt.duckdns.org:8080/ip_tracker/version.txt")[0].decode('ascii'))
        if newest_version > 0.1:
            return True
        else:
            return False
    except Exception as error:
        logging("failed update check; " , error)



'''funktion requestet ip von ifconfig.me'''
def external_ip_requester():
    try:
        ip = str(cmd("curl -s http://ifconfig.me/ip")[0]) #self made function cmd because noconsole error
        ip= ip[2:len(ip)-1]
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
def Pfad():
    return str(path.dirname(path.realpath(__file__)))


def send_text():
    Path = Pfad()
    with open(Path + "\\data.conf", "r") as data: #liest daten aus .conf file; Positionsabhängig!!!
        Data = data.readlines()
        for i in range(0,3):
            Data[i] = bdecode(Data[i])
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
    Path = Pfad()
    file_location = Path + "\\email.log"
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with open(file_location, "a+") as log:
            log.write(date + ";   " + TEXT + " \n")
    except Exception as nopen1:
        print("Couldn't write to file")
        print(nopen1)

def schedule_task(frequency, time):
    Path = Pfad()
    try:
        Tasks = str(cmd('SCHTASKS'))
        Tasks.index("ip_tracker")
        try:
            cmd('SCHTASKS /DELETE /TN "ip_tracker" /f')
        except Exception as error:
            logging("Couldnt delete Task; ", error)
    except:
        pass
    try:
        cmd('SCHTASKS /CREATE /SC ' + str(frequency) + ' /TN "ip_tracker" /TR "' + Path + '\\main.py" /ST ' + str(time))
        logging("Task wurde erstellt")
    except Exception as error:
        logging("Fehler beim erstellen von Task; ", error)


def  disable_task():
    try:
        cmd('SCHTASKS /CHANGE /TN "ip_tracker" /DISABLE')
        logging("Task disabled")
    except Exception as error:
        logging("Couldn't disable task; ", error)

def enable_task():
    try:
        cmd('SCHTASKS /CHANGE /TN "ip_tracker" /ENABLE')
        logging("Task enabled")
    except Exception as error:
        logging("Couldn't enable task; ", error)


def WriteToFile(email, password, receiver, ip):
    Path = Pfad()
    with open(Path + "\\data.conf", "w+") as file:
        file.writelines([email, "\n", password, "\n", receiver, "\n", ip])


