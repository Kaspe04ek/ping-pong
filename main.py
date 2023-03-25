from pygame import *
from random import randint
from time import sleep
 
img_ball = "ball.png" 
img_blue = "blue.png" 
img_red = "red.png" 
img_back = 'back3.jpg'

win_width = 600
win_height = 500
display.set_caption("ping-pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

font.init()
font2 = font.SysFont('Arial', 36)
font1 = font.SysFont('Arial' , 80)

lose = font2.render('ИГРОК ПЕРВЫЙ ПРОИГРАЛ!' , True , (180 , 0 , 0))
lose2 = font2.render('ИГРОК ВТОРОЙ ПРОИГРАЛ' , True , (180 , 0 ,0))

num1 = randint(1, 2)
num2 = randint(1, 2)

if num1 == 1:
    speed_x = -3
else:
    speed_x = 3

if num2 == 2:
    speed_y = -3
else:
    speed_y = 3


FPS = 60
finish = False
run = True


class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed , size_x, size_y, ):
       sprite.Sprite.__init__(self)
 
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)       
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
 
 
#класс главного игрока 1
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 130:
            self.rect.y += self.speed
 

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 130:
            self.rect.y += self.speed
 
 

        


 
 
#Создаём окошко

#создаём спрайты
Red_P1 = Player(img_red, 30 , 180, 5, 25, 150)
Blue_P2 = Player(img_blue, 535 , 180 ,  5 , 25 ,150)
Ball = GameSprite(img_ball , 275 ,225 , 5 , 50, 50 )
 

#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты

#Основной цикл игры:
 #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        #обновляем фон
        window.blit(background,(0,0))

        #производим движения спрайтов
        Red_P1.update_l()
        Blue_P2.update_r()
        Ball.update()
        Red_P1.reset()
        Blue_P2.reset()
        Ball.reset()

        random = randint(1,2)
        random2 = randint(1,2)

        Ball.rect.x += speed_x
        Ball.rect.y += speed_y

      
        if sprite.collide_rect(Red_P1 , Ball) or sprite.collide_rect(Blue_P2 , Ball):
            speed_x *= -1
            speed_y *= 1
        if Ball.rect.y > win_height-30 or Ball.rect.y < 0:
            speed_y *= -1
        if Ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (50 , 200))
        if Ball.rect.x < 0:
            finish = True
            window.blit(lose , (50 , 200))

        
        
    
        display.update()
    time.delay(30)