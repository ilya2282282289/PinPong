from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, speed,x, y, width=65, height=65):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (width, height))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_l(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        
        if keys_pressed[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed
        
class Player_r(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        
        if keys_pressed[K_s] and self.rect.y < 300:
            self.rect.y += self.speed

class Enemy(GameSprite):
    speedx = 3
    speedy = 3
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.y >= 400:
            self.speedy -= self.speedy + self.speedy
            finsih = False
        
        elif self.rect.x > 640:
            self.speedx -= self.speedx + self.speedx


window = display.set_mode((700, 500))
display.set_caption("Ping Pong")

background = transform.scale(image.load('fantasyforest.png'), (700, 500))

player_r = Player_r("platform_v.png", 7, 20, 200, 20, 200)
player_l = Player_l("platform_v.png", 7, 660, 200, 20, 200)

ball = Enemy("football.png", 3, 300, 200)

clock = time.Clock()
FPS = 60

game = True
finsih = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finsih:
        window.blit(background, (0,0))

        player_r.reset()
        player_l.reset()

        player_r.update()
        player_l.update()

        ball.reset()
        ball.update()
        clock.tick(FPS)
        display.update()






# #задай фон сцены
# background = transform.scale(image.load('background.png'), (700, 500))
# #создай 2 спрайта и размести их на сцене
# sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
# sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
# #обработай событие «клик по кнопке "Закрыть окно"»
# game = True
# clock = time.Clock()
# FPS = 60
# x1 = 100
# y1 = 300
# x2 = 300
# y2 = 300
# while game:
#     window.blit(background, (0,0))

#     window.blit(sprite1, (x1,y1))
#     window.blit(sprite2, (x2,y2))

#     keys_pressed = key.get_pressed()

#     for events in event.get():
#         if events.type == QUIT:
#             game = False

#     if keys_pressed[K_LEFT] and x1 > 5 :
#         x1 -= 10

#     if keys_pressed[K_RIGHT] and x1 <595:
#         x1 += 10

#     if keys_pressed[K_DOWN] and y1 <395:
#         y1 += 10

#     if keys_pressed[K_UP] and y1 >0 :
#         y1 -= 10

#     if keys_pressed[K_a] and x2 >-0:
#         x2 -=10

#     if keys_pressed[K_d]  and x2 <595:
#         x2 += 10

#     if keys_pressed[K_s] and y2 <395:
#         y2 += 10

#     if keys_pressed[K_w] and y2 >-0:
#         y2 -= 10

#     clock.tick(FPS)
#     display.update()
