from ipaddress import *
net = ip_network('240.144.182.134/255.255.248.0')
a = set()
for ip in net:
    ip_adr = f'{ip:b}'
    #ЕСЛИ ПИТОН < 3.11 ip_adr = ''.join([bin(int(i))[2:] for i in f'{ip}'.split(".")]) или     ip_adr = bin(int(ip))[2:]

    if (ip_adr.count('1')%5)== 0:
        a.add(ip_adr)
#
# print(len(a))
# for A in range(0,255):
    # net = ip_network(f'248.112.{A}.35/255.255.255.240',0)

    # for ip in net:
        # ip_adr =
        #ЕСЛИ ПИТОН < 3.11 ip_adr = ''.join([bin(int(i))[2:] for i in f'{ip}'.split(".")]) или     ip_adr = bin(int(ip))[2:]


#         if (ip_adr.count('1')%5)== 0:
#             a.add(ip_adr)
#
# print(len(a))
