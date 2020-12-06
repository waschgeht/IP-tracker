import ip_tracker.functions as f

ip = f.external_ip_requester()

email= input("please enter a username:")
password = input(" enter a password")

with open("data.conf", "w+") as file:
    file.writelines([email, "\n", password, "\n", ip])