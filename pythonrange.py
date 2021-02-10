
# for n in range (2,11):
#     user = input ("masukan nama anda    :")
#     print ("vlan " + str(n) + user)
#     print ("name VLAN_Python")
#     print ("name Python_VLAN_" + str(n))
f = open ('myswitches')
for IP in f:
    IP=IP.strip()
    print ("Configuring Switch " + (IP))
    HOST = IP
    print (HOST)