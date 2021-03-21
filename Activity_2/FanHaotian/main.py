import pygame
import sys
import pygame.freetype
import time
from word import *

pygame.init()  #初始化
#三种颜色的RGB值
BLACK=0,0,0
WHITE=255,255,255
GOLD=255,215,0
#初始化窗口大小
size=wide,height=600,600
screen=pygame.display.set_mode(size,pygame.FULLSCREEN)  #将窗口全屏显示

pygame.display.set_caption("word")   #更改窗口名称
info_Object=pygame.display.Info()  #找到窗口分辨率

#p1,p2,p3:分别为三种文字位置
p1=[info_Object.current_w/2.5,info_Object.current_h/2.5]
p2=[10,10]
p3=[info_Object.current_w-70,10]
#设定帧率
fps=3000
fclock=pygame.time.Clock()
#设置文字参数
f1=pygame.freetype.Font("C://Windows//Fonts//BELL.TTF",100)
f2=pygame.freetype.Font("C://Windows//Fonts//BELL.TTF",100)
f3=pygame.freetype.Font("C://Windows//Fonts//BELL.TTF",100)

s1=Read_file()
start=time.perf_counter()  #开始计时
#循环
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:   #点击事件
            if event.key==pygame.K_ESCAPE:  #点击Esc退出
                sys.exit()

    end=time.perf_counter()   #结束计时
    screen.fill(BLACK)
    i=round((end-start),2)
    if i==int(i):
        s1=Read_file()
    s2 = "Elapsed time: " + str(round(i, 2)) + " sec"
    s3 = "FPS:" + str(round(fclock.get_fps()))
    f1rech = f1.render_to(screen, p1,s1, fgcolor=WHITE, size=50)
    f2rech = f2.render_to(screen, p2, s2, fgcolor=GOLD, size=15)
    f3rech = f3.render_to(screen, p3, s3, fgcolor=GOLD, size=15)
    pygame.display.update()   #刷新屏幕
    fclock.tick(fps)   #控制帧率