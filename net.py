import os, re
var = os.popen('arp -an').read()
print(str(len(var.split('\n')))+" devices found")
print("MAC Addresses: ")
print("\n".join([x.split(' ')[3] for x in var.split('\n') if x != '']))