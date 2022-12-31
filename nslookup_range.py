#/usr/local/bin/python3

# nsrange.py resolve a list of hostnames to ipaddresses from file
# author: Simone Dellabora

import socket
import sys


f = open(sys.argv[1])

hosts = f.readlines()

print("\n" + "-" * 10, "Start nslookup", "-" * 10, "\n")

for hostname in hosts:
    try:
        ip = socket.gethostbyname(hostname.strip())
        print("\nHostname: {} ip address {}".format(hostname, ip))
    except:
        print("\nInvalid hostname: {}".format(hostname))
    
f.close()

print("\n" + "-" * 10, "End nslookup", "-" * 10, "\n")

