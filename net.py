import os, re
var = os.popen('nmap -sn {}/{}'.format(input("Enter Network Identifier: "), input("Enter subnet mask"))).read()
#var = os.popen('nmap -sn 192.168.0.17/24').read()
print("Hosts found: "+var.split('\n')[-2].split(' ')[5][1:])
print("MAC Addresses:")
print("\n".join([x.replace("MAC Address: ","")[:17].replace("Nmap done: 256 IP","") for x in var.split('\n')[1::3][1:]]))