import socket, pygame
from pygame.locals import *

host='192.168.1.245'
port=1234

server = (host,port)

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Client!!")

while True:
    connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection.connect(server)
    print("Connected to",host)
    connection.sendall(str.encode("Connection established"))

    data = connection.recv(2048).decode("utf-8")

    while True:
        if data:
            print("Received from server: ",repr(data))
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
            print("You pressed the right mouse button at ",event.pos)
