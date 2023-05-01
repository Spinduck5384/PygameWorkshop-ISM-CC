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
score = 0 

while run:
    keys = pygame.key.get_pressed()

    player = pygame.Rect(playerX,playerY, playerwidth, playerlength)
    
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_LEFT] == True and playerX >= 10:
        playerX -= 10
    if keys[pygame.K_RIGHT] == True and playerX <= 740:
        playerX += 10


    win.fill((0,0,0))

    if health > 0:

        time_counter = clock.tick(100)
        enemy_timer += time_counter

        if enemy_timer > 750:
            create_enemy()
            enemy_timer = 0 

        for enemy in enemy_db:

            if enemy[1] > 800:
                enemy_db.remove(enemy)
                score += 1
            
            enemyRect = pygame.Rect(enemy[0], enemy[1], 50, 50)

            if player.colliderect(enemyRect) == True:
                health -= 1

            #[X Pos, Y Pos, Width, Length, Color, Speed, ID]
            enemy[1] += enemy[-2]
            pygame.draw.rect(win, enemy[4], (enemy[0], enemy[1], 50, 50))
        
        f = open('data.txt', 'r')
        high_score = f.readline()
        f.close()

        if int(high_score) <= int(score):
            high_score = score
            f = open('data.txt', 'w')
            f.write(str(score))
            f.close()
        
        health_text = font.render("Health: " + str(health), False, (255, 0,0))
        win.blit(health_text, (550, 20))

        score_text = font.render("Score: " + str(score), False, (255,0,0))
        win.blit(score_text, (550,80))

        high_score_text = font.render("High Score: " + str(high_score), False, (255,0,0))
        win.blit(high_score_text, (550,50))

        pygame.draw.rect(win, playercolor, (playerX, playerY, playerwidth, playerlength))
    
    else:
        high_score_text = font.render("High Score: " + str(high_score), False, (255,0,0))
        score_text = font.render("Score: " + str(score), False, (255,0,0))
        end_text = font.render("Game Over!", False, (255,0,0))
        
        win.blit(end_text, (325, 370))
        win.blit(high_score_text, (325,400))
        win.blit(score_text, (325, 430))
    
    pygame.display.update()

pygame.quit()