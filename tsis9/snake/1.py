import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
Clock = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 20)

#Create a white screen 
screen = pygame.display.set_mode((800,800))
screen.fill(WHITE)
pygame.display.set_caption("Game")
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # каждый 1 секунд өткенін анықтайды

score = 0
speed = 5


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = (random.randint(10, SCREEN_WIDTH - 10))
        self.y = (random.randint(10, SCREEN_WIDTH - 10))
        self.radius = 10

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

    def generate(self):
        self.x = (random.randint(10, SCREEN_WIDTH - 10))
        self.y = (random.randint(10, SCREEN_WIDTH - 10))


class Food1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = (random.randint(10, SCREEN_WIDTH - 10))
        self.y = (random.randint(10, SCREEN_WIDTH - 10))
        self.radius = 10

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius)

    def generate(self):
        self.x = (random.randint(10, SCREEN_WIDTH - 10))
        self.y = (random.randint(10, SCREEN_WIDTH - 10))

class Big_Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = (random.randint(10, SCREEN_WIDTH - 10))
        self.y = (random.randint(10, SCREEN_WIDTH - 10))
        self.radius = 30

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

    def generate(self):
        self.x = (random.randint(10, SCREEN_WIDTH - 10))
        self.y = (random.randint(10, SCREEN_WIDTH - 10))

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 3
        self.elements = [[100,100], [110,100],[120,100]]
        self.radius = 5
        self.dx = 5
        self.dy = 0

        self.is_add = False
        
    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, BLUE, element, self.radius)
    def move(self):

        if self.is_add == True:
            self.add_to_snake()


        if self.elements[len(self.elements) - 1][0] < 10:
            self.dx = -self.dx
            # self.elements = self.elements[::-1]  # элементтерін кері бағытта ауыстырады
        elif self.elements[len(self.elements) - 1][0] > SCREEN_WIDTH - 10:
            self.dx = -self.dx # self.elements = self.elements[::-1]

        elif self.elements[len(self.elements) - 1][1] < 10 :
            self.dy = -self.dy # self.elements = self.elements[::-1]
        elif self.elements[len(self.elements) - 1][1] > SCREEN_HEIGHT - 10:
           self.dy = -self.dy # self.elements = self.elements[::-1]

        for i in range(0, self.size - 1):  #  0 1
            self.elements[i][0] = self.elements[i+1][0]
            self.elements[i][1] = self.elements[i+1][1]

        self.elements[len(self.elements) - 1][0] += self.dx
        self.elements[len(self.elements) - 1][1] += self.dy
        

    def eat(self, foodx, foody):
        x = self.elements[len(self.elements) - 1][0]
        y = self.elements[len(self.elements) - 1][1]
        
        if abs(x-foodx) <= 2*self.radius and abs(y-foody) <= 10:
            global score 
            score += 1
            return True
        return False
    def eat1(self, foodx, foody):
        x = self.elements[len(self.elements) - 1][0]
        y = self.elements[len(self.elements) - 1][1]
        
        if abs(x-foodx) <= 2*self.radius and abs(y-foody) <= 10:
            global score 
            score += 10
            return True
        return False
    def eat_big(self, foodx, foody):
        x = self.elements[len(self.elements) - 1][0]
        y = self.elements[len(self.elements) - 1][1]
        
        if abs(x-foodx) <= 35 and abs(y-foody) <= 35:
            global score 
            score += 3
            return True
        return False
    def add_to_snake(self):
        self.size += 1
        new_pointX = self.elements[0][0]-2*self.dx
        new_pointY = self.elements[0][1]-2*self.dy
        self.elements.append([new_pointX, new_pointY])
        self.is_add = False
        if self.size % 3 == 0:
            global speed
            speed += 1
 

snake1 = Snake()
food1 = Food()
big_food = Big_Food()
food2 = Food1()

timer = 0
time_on1 = False
time_on2 = False
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # каждый 1 секунд өткенін анықтайды

#Game Loop
while True:
    #Cycles through all events occurring  
    for event in pygame.event.get(): 
        if event.type == INC_SPEED and time_on1 == True:  # каждый 1 секнд өткен сайын, жылдамдық += 0,5
                timer += 1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT:
                snake1.dx = speed
                snake1.dy = 0
            elif event.key == pygame.K_LEFT:
                snake1.dx = -speed
                snake1.dy = 0
            elif event.key == pygame.K_UP:
                snake1.dx = 0
                snake1.dy = -speed
            elif event.key == pygame.K_DOWN:
                snake1.dx = 0
                snake1.dy = speed
    if snake1.eat(food1.x, food1.y) == True:
        snake1.is_add = True
        food1.generate()
    if snake1.eat1(food2.x, food2.y):
        time_on = False
        snake1.is_add = True
        food2.generate()
    if snake1.eat_big(big_food.x, big_food.y):
        time_on = False
        snake1.is_add = True
        big_food.generate()
    screen.fill(BLACK)
    scores = font.render(str(score), True, WHITE) # ұпайдың жазуы
    screen.blit(scores, (700,50))
    

    
    snake1.draw()
    food1.draw()
    if timer >= 5:
        time_on1 = False
    if timer % 5 == 0 and score > 0 and score % 5 == 0 :
        time_on1 = True
    if timer % 1 == 0 and score > 0 and score % 1 == 0 :
        time_on2 = True
    if time_on1 == True:
        big_food.draw()
    if time_on2 == True:
        food2.draw()

    snake1.move()
         
    pygame.display.update()
    Clock.tick(FPS)
    
pygame.quit()