import pygame
import random
pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Code Club Game")

run = True

playerX = 400
playerY = 750
playerlength = 50
playerwidth = 50
playercolor = (255,0,0)

font = pygame.font.Font(None, 40)

clock = pygame.time.Clock()
enemy_timer = 0

enemy_db = [

]

enemy_id = 0

def create_enemy():
    global enemy_id

    speed = random.randint(5,20)
    enemyX = random.randint(10,740)
    enemyY = -50
    red = random.randint(0,250)
    green = random.randint(0,250)
    blue = random.randint(0,250)
    enemycolor = (red, green, blue)
    enemy_id += 1
    enemy_id_copy = enemy_id

    enemy_db.append([enemyX, enemyY, 50, 50, enemycolor, speed, enemy_id_copy])
    #[X Pos, Y Pos, Width, Length, Color, Speed, ID]

health = 100

while run:
    keys = pygame.key.get_pressed()

    player = pygame.Rect(playerX,playerY, playerwidth, playerlength)
    
    pygame.time.delay(100)
    

    time_counter = clock.tick(100)
    enemy_timer += time_counter

    if enemy_timer > 750:
        create_enemy()
        enemy_timer = 0 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_LEFT] == True and playerX >= 10:
        playerX -= 10
    if keys[pygame.K_RIGHT] == True and playerX <= 740:
        playerX += 10


    win.fill((0,0,0))

    for enemy in enemy_db:

        if enemy[1] > 800:
            enemy_db.remove(enemy)
        
        enemyRect = pygame.Rect(enemy[0], enemy[1], 50, 50)

        if player.colliderect(enemyRect) == True:
            health -= 1

        #[X Pos, Y Pos, Width, Length, Color, Speed, ID]
        enemy[1] += enemy[-2]
        pygame.draw.rect(win, enemy[4], (enemy[0], enemy[1], 50, 50))
    
    health_text = font.render("Health: " + str(health), False, (255, 0,0))
    win.blit(health_text, (550, 20))

    pygame.draw.rect(win, playercolor, (playerX, playerY, playerwidth, playerlength))
    
    pygame.display.update()

pygame.quit()