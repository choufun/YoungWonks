import socket

HOST = socket.gethostbyname("google.com")
PORT = 80

webpage = ''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall('GET / HTTP/1.1\r\n\r\n'.encode())
    while True:
        data = s.recv(1).decode('utf-8')
        if not data:
            break
    print(data, end='')

    

