import pygame

pygame.init()

# Window Size of 500 width, 500 height
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("pirate game")


walkRight = [pygame.image.load('source/R1.png'), pygame.image.load('source/R2.png'),
pygame.image.load('source/R3.png'),pygame.image.load('source/R4.png'),
pygame.image.load('source/R5.png'),pygame.image.load('source/R6.png'),
pygame.image.load('source/R7.png'),pygame.image.load('source/R8.png'),
pygame.image.load('source/R9.png')]

walkLeft = [pygame.image.load('source/L1.png'), pygame.image.load('source/L2.png'),
pygame.image.load('source/L3.png'),pygame.image.load('source/L4.png'),
pygame.image.load('source/L5.png'),pygame.image.load('source/L6.png'),
pygame.image.load('source/L7.png'),pygame.image.load('source/L8.png'),
pygame.image.load('source/L9.png')]

bg = pygame.image.load('source/bg.jpg')
char = pygame.image.load('source/standing.png')


# 캐릭터의 위치와 크기
x = 50
y = 400
width = 40
height = 60
velocity = 10

clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height
#--------------초기 세팅 값--------------    
        self.velocity = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def move(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.left: 
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        
        elif self.right: 
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        
        else:
            win.blit(char, (self.x, self.y))


def redrawGameWindow():
    win.blit(bg, (0,0)) # This will draw our background image at (0,0)
    man.move(win)
    pygame.display.update()


man = Player(x=200, y=410, width=64, height=64)
run = True
while run:
    clock.tick(27) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False

    elif keys[pygame.K_RIGHT] and x < 500 - man.velocity - man.width:
        man.x += man.velocity
        man.left = False 
        man.right = True

    else:
        man.left = False 
        man.right = False 
        man.walkCount = 0

    if not(man.isJump):
        # if keys[pygame.K_UP] and y > velocity:
        #     y -= velocity
        
        # if keys[pygame.K_DOWN] and y < 500 - velocity - height:
        #     y += velocity

        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.3
            man.jumpCount -= 1
        else:
            man.jumpCount = 10
            man.isJump = False

    redrawGameWindow() 

pygame.quit()
