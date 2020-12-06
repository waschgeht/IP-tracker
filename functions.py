import os


'''funktion requestet ip von ifconfig.me'''
def external_ip_requester():
    try:
        ip = str(os.popen("curl http://ifconfig.me/ip").read()) #.popen erzeugt keine Ausgabe am Screen
        int(ip[0]) #testet ob ausgabe eine IP ist. Erzeugt fehler wenn falsch und läuft in except block
        return ip
    except:
        print("Couldnt get ip from http://ifconfig.me/ip")
        raise SystemExit(0) #schließt das programm komplett

