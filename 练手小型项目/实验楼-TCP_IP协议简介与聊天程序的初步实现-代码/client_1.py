import socket

host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

print(s.recv(1024).decode())

for data in ['Michael', 'Tracy', 'Sarah']:
    s.send(data.encode())
    print(s.recv(1024).decode())
s.send('exit'.encode())
s.close()

