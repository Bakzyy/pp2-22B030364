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
#Create a white screen 
screen = pygame.display.set_mode((800,800))
screen.fill(WHITE)
pygame.display.set_caption("Game")
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # каждый 1 секунд өткенін анықтайды


score = 0
speed = 5

font = pygame.font.SysFont("Verdana", 20)

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
    
    def add_to_snake(self):
        self.size += 1
        new_pointX = self.elements[0][0]-2*self.dx
        new_pointY = self.elements[0][1]-2*self.dy
        self.elements.append([new_pointX, new_pointY])
        self.is_add = False
        if self.size % 3 == 0:
            global speed
            speed += 1
 

snake = Snake()
food = Food()

# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)  # каждый 1 секунд өткенін анықтайды

#Game Loop
while True:
    #Cycles through all events occurring  
    for event in pygame.event.get(): 
        # if event.type == INC_SPEED: # каждый 1 секнд өткен сайын, жылдамдық += 0,5
        #         speed += 1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT:
                snake.dx = speed
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -speed
                snake.dy = 0
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -speed
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = speed
    if snake.eat(food.x, food.y) == True:
        snake.is_add = True
        food.generate()
   
    screen.fill(BLACK)
   
    scores = font.render(str(score), True, WHITE) # ұпайдың жазуы
    screen.blit(scores, (700,50))
    
    snake.draw()
    food.draw()

    snake.move()
         
    pygame.display.update()
    Clock.tick(FPS)
    
pygame.quit()