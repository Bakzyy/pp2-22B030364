import pygame as pg
import datetime

pg.init()
WIDTH = 1400
HEIGHT = 1050
FPS = 60
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Clock')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
background = pg.transform.scale(pg.image.load('/Users/bakustar2005/Documents/pp2/tsis7/images/main-clock.png'), (WIDTH, HEIGHT))

font = pg.font.SysFont("Times New Roman", 30)

rhand = pg.image.load('/Users/bakustar2005/Documents/pp2/tsis7/images/right-hand.png')
lhand = pg.image.load('/Users/bakustar2005/Documents/pp2/tsis7/images/left-hand.png')

def blit_rotate_center(image, x0, y0, angle):
    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = (x0, y0)).center)
    screen.blit(rotated_image, new_rect)


running = True
while running:
    clock.tick(FPS)
    screen.blit(background, (0, 0))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    time = datetime.datetime.now()
    minute = time.minute
    second = time.second
    
    screen.blit(background, (0, 0))
    text = font.render(f'The time is now: {minute}:{second}', True, BLUE)
    
    blit_rotate_center(rhand, WIDTH // 2 - rhand.get_width() // 2, HEIGHT // 2 - rhand.get_height()//2,
                       (-6*(minute + second) / 60) - 148)
    blit_rotate_center(lhand, WIDTH // 2 - lhand.get_width() // 2, HEIGHT // 2 - lhand.get_height() // 2,
                       (-6*second) + 92)  
    screen.blit(text, (250, 550))

    pg.display.update()

pg.quit()

exit()