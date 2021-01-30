# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import pygame

import randomword

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("wordlist")
font = pygame.font.SysFont("arial", 32)
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
words = randomword.get_random_word()
rword = pygame.USEREVENT + 1
pygame.time.set_timer(rword, 1000)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == rword:
            words = randomword.get_random_word()

    end_time = pygame.time.get_ticks()  # gets the current program time

    time = (end_time - start_time) // 1000  # count program time
    fps = int(clock.get_fps())

    screen.fill("black")  # output text content
    text_surface1 = font.render("Time:" + str(time), True, "yellow")
    screen.blit(text_surface1, (0, 0))
    text_surface2 = font.render("fps:" + str(fps), True, "white")
    screen.blit(text_surface2, (700, 0))

    clock.tick(60)
    w = font.render(str(words), True, 'green')
    screen.blit(w, (300, 200))

    pygame.display.update()
