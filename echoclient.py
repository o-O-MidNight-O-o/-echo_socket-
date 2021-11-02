
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket:
    socket.connect((HOST,PORT))
    socket.sendall(b'hello, world')
    data = socket.recv(1024)

print('received',repr(data))

