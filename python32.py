import getpass
import telnetlib

HOST = "192.168.122.146"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"no vlan 2\n")
tn.write(b"name Python_VLAN_2\n")
tn.write(b"no vlan 3\n")
tn.write(b"name Python_VLAN_3\n")
tn.write(b"no vlan 4\n")
tn.write(b"name Python_VLAN_4\n")
tn.write(b"no vlan 5\n")
tn.write(b"name Python_VLAN_5\n")
tn.write(b"no vlan 6\n")
tn.write(b"name Python_VLAN_6\n")
tn.write(b"no vlan 7\n")
tn.write(b"name Python_VLAN_7\n")
tn.write(b"no vlan 8\n")
tn.write(b"name Python_VLAN_8\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
