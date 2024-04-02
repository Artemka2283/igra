#Создай собственный Шутер!

from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x_player, y_player, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image)
                                     , (65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_player
        self.rect.y = y_player
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        button = key.get_pressed()
        if button[K_LEFT] and self.rect.x > 10:
            self.rect.x -=self.speed
        if button[K_RIGHT] and self.rect.x < win_width - 60:
            self.rect.x +=self.speed
        if button[K_UP] and self.rect.y > 10:
            self.rect.y -=self.speed
        if button[K_DOWN] and self.rect.y < win_height - 50: 
            self.rect.y +=self.speed
    def fire(self):
        
        bullet = Bullet('Kirieshki.png', self.rect.centerx, self.rect.top, 15,20, 10)
        bullets.add(bullet)
Players = sprite.Group()
player1 = Player('Mazelov.png', 450, 417, 50, 10 - 80, 4)
player2 = Player('Mazelov.png', 490, 417, 50, 10 - 80, 4)
player3 = Player('Mazelov.png', 550, 417, 50, 10 - 80, 4)
chubriks = sprite.Group()

Players.add(player1)
Players.add(player2)
Players.add(player3)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("galaxy")
background = transform.scale(image.load("Moscow.jpg"),
                              (win_width, win_height))
proshli = 0
sbili = 0
health = 10
class Enemy(GameSprite):
    direction = "nalevo"
    def update(self):
        self.rect.y += self.speed
        global proshli
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(80, 620)
            self.speed = randint(1,3)
            proshli += 1
class Asteriod(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(80, 620)
            self.speed = randint(1,3)
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

clock = time.Clock()
for i in range (1, 6):
    chubrik = Enemy('Kussia88.png', randint(80, 620), 10, 50, 50, randint(1, 3))
    chubriks.add(chubrik)
bullets = sprite.Group()
asteroids = sprite.Group()
for i in range(1, 5):
    asteroid = Asteriod('5opka.png', randint(30, win_width - 30), -40, 100 , 110 , randint(1, 7))
    asteroids.add(asteroid)

font.init()
font = font.SysFont('Calibri', 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (188, 0 ,0))

mixer.init()
mixer.music.load('Dabstep.mp3')
mixer.music.play()
zvuk_fire = mixer.Sound('fire.ogg')
game = True
finish = False
while game:
    for knopka in event.get():
        if knopka.type == QUIT:
            game = False
        elif knopka.type == KEYDOWN:
            if knopka .key == K_SPACE:
                zvuk_fire.play
                player1.fire()
                player2.fire()
                player3.fire()

    if finish != True:
        window.blit(background,(0,0))
        text = font.render('Счёт:' + str(sbili), 1, (255, 255, 255))
        window.blit(text, (10, 20)) 
        text_lost = font.render('Пропущено:' + str(proshli), 1, (255, 255, 255))
        window.blit(text_lost, (10,60))
        Players.update()
        Players.draw(window)
        chubriks.update()
        bullets.update()
        chubriks.draw(window)
        bullets.draw(window)
        display.update()
        asteroids.update()
        asteroids.draw(window)
        showdawn = sprite.groupcollide(chubriks, bullets, True, True)
        for down in showdawn:
            sbili += 1 
            chubrik = Enemy('Kussia88.png', randint(80, 620), 10, 50, 50, randint(1, 2))
            chubriks.add(chubrik)
            if sprite.groupcollide(Players, chubriks, False, False):
                sprite.groupcollide(Players, chubriks, True, True)
                health -= 2
            if sprite.groupcollide(Players, asteroids, False, False):
                sprite.groupcollide(Players, asteroids, True, True)
                    #!!!!!!!!!!!!!!ДОПИШИТЕ САМИ!!!!!!!!!!!!!!!!!!
        if health <= 1 or proshli > 30:
            finish = True
            window.blit(lose, (200, 200))
        if sbili > 100:
            finish = True
            window.blit(win, (200, 200))
        display.update()
    clock.tick(120)
    