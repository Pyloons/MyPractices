import socket
import time
import threading


def tcplink(sock, addr):
    print('Accept new connection form {}:{}...'.format(addr[0], str(addr[1])))
    sock.send('Welcome!'.encode())
    while True:
        data = sock.recv(1024).decode()
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, {}!'.format(data).encode())
    sock.close()
    print('Connection from {}:{} closed.'.format(addr[0], str(addr[1])))

host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

