import pygame
import sys
import randomword

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
myFont = pygame.font.Font(None, 30)
word = randomword.get_random_word()
MYEVENT01 = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENT01, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MYEVENT01:
            word = randomword.get_random_word()

    end_time = pygame.time.get_ticks()
    time = (end_time - start_time) // 1000
    fps = int(clock.get_fps())

    screen.fill("white")
    textImage = myFont.render("time:" + str(time), True, "violet")
    screen.blit(textImage, (2, 2))
    textImage2 = myFont.render("fps:" + str(fps), True, "violet")
    screen.blit(textImage2, (530, 2))
    textImage3 = myFont.render(str(word), True, 'black')
    screen.blit(textImage3, (200, 170))

    clock.tick(60)
    pygame.display.update()

