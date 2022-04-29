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

bulletSound = pygame.mixer.Sound('source/bullet.mp3')
hitSound = pygame.mixer.Sound('source/hit.mp3')

music = pygame.mixer.music.load('source/music.mp3')
pygame.mixer.music.play(-1)


# 캐릭터의 위치와 크기
x = 50
y = 400
width = 40
height = 60
velocity = 10

clock = pygame.time.Clock()

class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = facing * 8 # 음수면 왼쪽, 양수면 오른쪽
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
    
    

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
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def move(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not(self.standing):
            if self.left: 
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            
            elif self.right: 
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y +11, 29, 52)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class Enemy(object):
    walkRight = [pygame.image.load('source/R1E.png'), pygame.image.load('source/R2E.png'),
    pygame.image.load('source/R3E.png'),pygame.image.load('source/R4E.png'),
    pygame.image.load('source/R5E.png'),pygame.image.load('source/R6E.png'),
    pygame.image.load('source/R7E.png'),pygame.image.load('source/R8E.png'),
    pygame.image.load('source/R9E.png'),pygame.image.load('source/R10E.png'), pygame.image.load('source/R11E.png')]

    walkLeft = [pygame.image.load('source/L1E.png'), pygame.image.load('source/L2E.png'),
    pygame.image.load('source/L3E.png'),pygame.image.load('source/L4E.png'),
    pygame.image.load('source/L5E.png'),pygame.image.load('source/L6E.png'),
    pygame.image.load('source/L7E.png'),pygame.image.load('source/L8E.png'),
    pygame.image.load('source/L9E.png'),pygame.image.load('source/L10E.png'),pygame.image.load('source/L11E.png') ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.path = [x, end]
        self.walkCount = 0
        self.velocity = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10 # 헬스가 0이되면 Visible False
        self.visible = True # False => 고블린 죽음

    def draw(self, win):
        self.move()
        if self.visible == True:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            
            if self.velocity > 0 :
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) # 전체 체력
            pygame.draw.rect(win, (0,128,9), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10)) # 맞은 후 체력
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)


    def move(self):
        if self.velocity > 0:
            if self.x < self.path[1] + self.velocity: 
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.x += self.velocity
                self.walkCount = 0 
        else: #왼쪽으로 가는 경우
            if self.x > self.path[0] - self.velocity:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.x += self.velocity
                self.walkCount = 0
    
    def hit(self):
        hitSound.play()
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False 


def redrawGameWindow():
    win.blit(bg, (0,0)) # This will draw our background image at (0,0)
    man.move(win)
    goblin.draw(win)
    text = font.render("Score: " + str(score), 1, (0,0,0)) 
    win.blit(text, (330, 10))
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


man = Player(x=200, y=410, width=64, height=64)
goblin = Enemy(x=100, y=410, width=64, height=64, end=350)
run = True
bullets = []
score = 0
font = pygame.font.SysFont('comicsans', 30, True)

while run:
    clock.tick(27) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets: 
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LCTRL]:
        bulletSound.play()
        if man.left:
            facing = -1 
        else:
            facing = 1
        if len(bullets) < 5: 
            bullets.append(Projectile(round(man.x+man.width//2), round(man.y + man.height//2), 6, (0,0,0), facing))

    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False
        man.standing = False

    elif keys[pygame.K_RIGHT] and x < 500 - man.velocity - man.width:
        man.x += man.velocity
        man.left = False 
        man.right = True
        man.standing = False

    else:
        man.standing = True
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
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) *0.5 * neg
            man.jumpCount -= 1
        else:
            man.jumpCount = 10
            man.isJump = False

    redrawGameWindow() 
 
pygame.quit()
