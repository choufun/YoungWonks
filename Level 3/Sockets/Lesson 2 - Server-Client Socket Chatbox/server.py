import socket

host = ''
port = 1234

client = (host,port)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(client)

print("Socket binded to", port)

backlog = 5
s.listen(backlog)
conn,addr = s.accept()
print("Socket is listening")
print("Got connection from", addr)

while True:
    name = input("Hello, say something to the client")
    print("Waiting for client's response")

    conn.send(name.encode())
    data = conn.recv(1024).decode('utf-8')
    print("Received from client address: ", addr)
    print("Message received: ",data)

conn.close()
