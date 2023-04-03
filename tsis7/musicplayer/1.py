import pygame as pg

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((500, 500))
pg.display.set_caption('Apple music')

musics = ['/Users/bakustar2005/Documents/pp2/tsis7/music/Maga_Poslednij_roman.mp3','/Users/bakustar2005/Documents/pp2/tsis7/music/vitya-ak-v-x-v-prince-na-2-ih-mp3.mp3','/Users/bakustar2005/Documents/pp2/tsis7/music/Bakr - Очи.mp3']

pg.mixer.music.load('/Users/bakustar2005/Documents/pp2/tsis7/music/Maga_Poslednij_roman.mp3')
pg.mixer.music.play()

SONG_END = pg.USEREVENT + 1
pg.mixer.music.set_endevent(SONG_END)

now = 0
def queue(music):
    global now 
    if music == True:
        now += 1
        if now >= len(musics):
            now = 0
        pg.mixer.music.load(musics[now])
        pg.mixer.music.play()   
    else:
        now -= 1
        if now < 0:
            now = len(musics) - 1
    pg.mixer.music.load(musics[now])  
    pg.mixer.music.play()          


done = False 
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == SONG_END:
            print('The Song Ended!')    
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            pg.mixer.music.pause()
        if event.type == pg.KEYDOWN and event.key == pg.K_UP:
            pg.mixer.music.unpause()
        if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            music =  True
            queue(music)
        if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            music = False
            queue(music)    
    screen.fill((225, 225, 225))
    font = pg.font.Font(None, 40)
    text1 = font.render('1.Maga_Poslednij_roman', True, (255, 100, 180))
    text2 = font.render('2.vitya-ak-v-x-v-prince-na-2-ih-mp3.', True, (0, 255, 255))
    text3 = font.render('3.Bakr - Очи', True, (255, 255, 0))
    text4 = font.render('   <<  -----  >>', True, (240, 0, 255))
    screen.blit(text1, [30, 100])
    screen.blit(text2, [30, 140])
    screen.blit(text3, [30, 180])
    screen.blit(text4, [150, 220])
    pg.display.flip()

pg.quit()