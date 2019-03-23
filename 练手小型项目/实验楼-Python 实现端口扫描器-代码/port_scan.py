#!/usr/bin/python
# _*_ conding: utf-8 _*_

import sys
import thread
from socket import *


def tcp_test(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        lock.acquire()
        print("Opened Port:", port)
        lock.release()

if __name__ == '__main__':
    host = sys.argv[1]
    start_port, end_port = sys.argv[2].split('-')
    target_ip = gethostbyname(host)
    
    lock = thread.allocate_lock()
    for port in range(int(start_port), int(end_port)):
        thread.start_new_thread(tcp_test, (port,))

