# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
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
speed = 1000  # 初始速度1000
pygame.time.set_timer(rword, speed)

a = 0

color_list = []  # 存储渐变色
color_list2 = []  # 存储渐变色相反色

# 从红到黄
for g in range(0, 256):
    color_list.append((255, g, 0))
    color_list2.append((0, 255 - g, 255))

# 从黄到绿
for r in range(255, -1, -1):
    color_list.append((r, 255, 0))
    color_list2.append((255 - r, 0, 255))

# 从绿到青
for b in range(0, 256):
    color_list.append((0, 255, b))
    color_list2.append((255, 0, 255 - b))

# 从青到蓝
for g in range(255, -1, -1):
    color_list.append((0, g, 255))
    color_list2.append((255, 255 - g, 0))

# 从蓝到紫
for r in range(0, 256):
    color_list.append((r, 0, 255))
    color_list2.append((255 - r, 255, 0))

# 从紫到红
for g in range(255, -1, -1):
    color_list.append((255, 0, g))
    color_list2.append((0, 255, 255 - g))

color = pygame.USEREVENT
pygame.time.set_timer(color, speed)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 按键事件
            if event.key == pygame.K_LEFT:  # 左方向键事件
                if speed - 100 < 15:  # 限制最高速度
                    speed = 15
                    pygame.time.set_timer(rword, speed)
                else:
                    speed = speed - 100  # 加速100
                    pygame.time.set_timer(rword, speed)
            elif event.key == pygame.K_RIGHT:  # 右方向键事件
                if speed + 100 > 10000:  # 限制最低速度
                    speed = 10000
                    pygame.time.set_timer(rword, speed)
                else:
                    speed = speed + 100  # 减速100
                    pygame.time.set_timer(rword, speed)
            print(event)
        elif event.type == color:
            if a <= 255 + 255 + 255 + 255 + 255 + 255:  # 渐变色数组上限
                colors = color_list[a]
                colors2 = color_list2[a]
                a = a + 1
            else:
                a = 0  # 重置渐变色数组

            pygame.time.set_timer(color, speed)
        elif event.type == rword:
            words = randomword.get_random_word()

    end_time = pygame.time.get_ticks()  # gets the current program time
    colors = color_list[a]
    colors2 = color_list2[a]
    time = (end_time - start_time) // 1000  # count program time
    fps = int(clock.get_fps())
    screen.fill(colors)
    # output text content
    text_surface1 = font.render("Time:" + str(time), True, "black")
    screen.blit(text_surface1, (0, 0))
    text_surface2 = font.render("fps:" + str(fps), True, "black")
    screen.blit(text_surface2, (700, 0))

    clock.tick(60)
    w = font.render(str(words), True, colors2)
    screen.blit(w, (300, 200))
    text_speed = font.render("Speed:" + str(speed), True, "black")  # 显示速度
    screen.blit(text_speed, (250, 300))
    speed_what = font.render("ms/word", True, "black")  # 显示速度单位
    screen.blit(speed_what, (450, 300))

    pygame.display.update()
