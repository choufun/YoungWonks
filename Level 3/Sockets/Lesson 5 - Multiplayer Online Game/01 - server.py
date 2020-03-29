import socket, pygame
from pygame.locals import *

host = ''
port = 1234
client = (host,port)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(client)

print("Socket binded to", port)

backlog = 1
server.listen(backlog)

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Server!!")

while True:
    print(server.getsockname()[0],"is waiting for connection")
    connection,address = server.accept()
    
    print("Socket is listening")
    print("Got connection from", address)
    
    connection.sendall(str.encode("Pygame started"))
    
    data = connection.recv(1024).decode('utf-8')
    
    while True:
        if data:
            print("Received from client address: ", address)
            print("Message received: ",data)
            data = None
        else:
            print("No more data.")
            break
        
    connection.close()
    print("Connection closed")
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("You pressed the left mouse button at",event.pos)
