import socket

host='192.168.1.245'
port=1234

server = (host,port)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(server)

while True:
    data = s.recv(1024)
    print("Received from server",repr(data))
    message = input("Say something to server: ")
    s.send(message.encode())
s.close()
