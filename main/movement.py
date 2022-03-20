import pygame

pygame.init()

# Window Size of 500 width, 500 height
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Movement Practice")

# 캐릭터의 위치와 크기
x = 50
y = 50
width = 40
height = 60
velocity = 5

run = True
while run:
    pygame.time.delay(100) # This will delay the game the given amount of milliseconds.
    # 0.1 seconds in our case
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    print(keys)

    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.display.update() # rectangle을 볼수 있게 해줌 
pygame.quit()
