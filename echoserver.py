
import socket


HOST = socket.gethostbyname(socket.gethostname()) #" "
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket:
    socket.bind((HOST,PORT))
    
    socket.listen()
    conn , addr = socket.accept()
    
    with conn:
        print("connected by",addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data) #echo back

