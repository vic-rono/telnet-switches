import getpass
import telnetlib

HOST = ''
user = input("Enter your  username: ")
password = getpass.getpass()

file = open ('switches')


for IP in file:
    IP=IP.strip()
    print ("Configuring Switch " + (IP))
    HOST = IP
    telnet = telnetlib.Telnet(HOST)
    telnet.read_until(b"Username: ")
    telnet.write(user.encode('ascii') + b"\n")
    if password:
       telnet.read_until(b"Password: ")
       telnet.write(password.encode('ascii') + b"\n")
       telnet.write(b"conf t\n")

    for x in range(2,21):
        telnet.write(b"vlan " + str(x).encode('ascii') + b"\n")
        telnet.write(b"name VLAN_" + str(x).encode('ascii') + b"\n")

    telnet.write(b"end\n")
    telnet.write(b"exit\n")
    print(telnet.read_all().decode('ascii'))
