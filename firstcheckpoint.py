import pygame
pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Code Club Game")

run = True

playerX = 400
playerY = 400
playerlength = 50
playerwidth = 50
playercolor = (255,0,0)

while run:
    pygame.time.delay(100)
    
    player = pygame.Rect(playerX,playerY, playerwidth, playerlength)
    
    
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))

    pygame.draw.rect(win, playercolor, (playerX, playerY, playerwidth, playerlength))
    
    pygame.display.update()

pygame.quit()