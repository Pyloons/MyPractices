#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from socket import *


host = sys.argv[1]
start_port, end_port = sys.argv[2].split('-')

target_ip = gethostbyname(host)
opened_ports = []

for port in range(int(start_port), int(end_port)):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        opened_ports.append(port)

print("Opened ports:")

for i in opened_ports:
    print(i)

