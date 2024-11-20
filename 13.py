from ipaddress import *



for mask in range(33):
    net = ip_network(f"111.91.192.0/{mask}", 0)
    ip_adr = f'{mask}'
    if ip_adr == '111.91.200.28':
        print(ip_adr)
