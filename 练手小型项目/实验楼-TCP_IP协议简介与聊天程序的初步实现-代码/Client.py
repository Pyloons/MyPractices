import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
print("linked")
info = ''
while info != "exit":
    print("From Others: " + info)
    send_mes = input()
    s.send(send_mes.encode())
    if send_mes == "exit":
        break
    info = s.recv(1024).decode()
s.close()

