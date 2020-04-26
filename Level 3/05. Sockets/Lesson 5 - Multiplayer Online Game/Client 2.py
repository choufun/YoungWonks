import socket

HOST = '192.168.1.245'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall('Connection establish'.encode())
    while True:
        data = s.recv(1024).decode()
        print('Received', data)
        if not data:
            break
        s.sendall(input('Enter: ').encode())
    

