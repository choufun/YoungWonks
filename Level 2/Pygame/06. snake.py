import pygame,random
from pygame.locals import*
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("snake")
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

#defining variables

foodx = (random.randint(0,600)//20)*20
foody = (random.randint(0,600)//20)*20
snakex = (random.randint(0,600)//20)*20
snakey = (random.randint(0,600)//20)*20

snakelist = [[snakex,snakey]]

fps = pygame.time.Clock()

dx = 0
dy = 0

game = True

while game:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            #exit()
           
        elif event.type == KEYDOWN:
            if event.key == K_d: #right
                dx = 20
                dy = 0
            elif event.key == K_a: #left:
                dx = -20
                dy = 0
            elif event.key == K_w: #up:
                dx = 0
                dy = -20
            elif event.key == K_s: #down:
                dx = 0
                dy = 20

    screen.fill(black)

    pygame.draw.rect(screen,red,(foodx,foody,20,20))

    for segment in snakelist:
        pygame.draw.rect(screen,green,segment+[20,20])
       
    pygame.display.update()

    if snakelist[0] == [foodx, foody]:
        print("ate FOOD")
        snakelist.insert(0,[snakelist[0][0]+dx,snakelist[0][1]+dy])
        #print(snakelist)
        
        foodx = (random.randint(0,600)//20)*20
        foody = (random.randint(0,600)//20)*20
        
    snakelist.insert(0,[snakelist[0][0]+dx,snakelist[0][1]+dy])
    snakelist.pop()

    fps.tick(8)




