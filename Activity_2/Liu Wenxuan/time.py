import pygame
import sys
import randomword

pygame.init()

background = pygame.image.load('1.jpeg')
b_rect = background.get_rect()
color = (0,0,0)
rword = pygame.USEREVENT + 1                        #change word
pygame.time.set_timer(rword,1000)                   #every second
clock = pygame.time.Clock
words = randomword.get_random_word()                #get random word
start_time = pygame.time.get_ticks()                #get start time
size = weight , hight = 1000,600
font = pygame.font.SysFont("fangsong", 40)
font2 = pygame.font.SysFont("songti",100)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("activity2")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == rword:
            words = randomword.get_random_word()                    #change word event

    end_time = pygame.time.get_ticks()                              #get game time
    t = (end_time - start_time) // 1000
    fps = int(clock.get_fps())                                      #get fps

    text_surface = font.render("时间:" + str(t), True, "black")
    #screen.fill(b_rect)
    screen.blit(background,b_rect)
    screen.blit(text_surface, (0, 0))
    text_fps = font.render('fps:' + str(fps) , True , 'black')
    screen.blit(text_fps , (870 , 0))
    w = font2.render(str(words),True,'black')
    screen.blit(w,(350,220))
    clock.tick(60)                                                  #Define default fps
    pygame.display.update()