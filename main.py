import ip_tracker.functions as f


def Main():
    ip = f.external_ip_requester()
    input("Programstart, pleas press enter!")
    email= input("please enter your email:")
    password = input(" enter the password:")
    receiver = input("please enter the receifing Email adress:")
    with open("data.conf", "w+") as file:
        file.writelines([email, "\n", password, "\n", ip, "\n", receiver])
    #f.send_text()