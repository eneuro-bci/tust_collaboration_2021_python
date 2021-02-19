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
screen=pygame.display.set_mode(size)  #将窗口全屏显示

pygame.display.set_caption("word")   #更改窗口名称
info_Object=pygame.display.Info()  #找到窗口分辨率

#p1,p2,p3:分别为三种文字位置
#p1=[0,0]
p1=[info_Object.current_w/2.5,info_Object.current_h/2.5]
p2=[10,10]
p3=[info_Object.current_w-70,10]
#设定帧率
fps=3000
fclock=pygame.time.Clock()
#设置文字参数
f1=pygame.freetype.Font("C://Windows//Fonts//Arial.ttf",100)
f2=pygame.freetype.Font("C://Windows//Fonts//Arial.ttf",100)
f3=pygame.freetype.Font("C://Windows//Fonts//Arial.ttf",100)
f1_size=50
f2_size=15
f3_size=15
f_color=pygame.Color("white")
back_color=pygame.Color("black")
s1=Read_file()
j=1
p=0,0
n_word=1
n_words=1
word_time=0
start=time.perf_counter()  #开始计时
#循环
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:   #点击事件
            if event.key==pygame.K_ESCAPE:  #点击Esc退出
                sys.exit()
            elif event.key==pygame.K_SPACE:
                j*=-1

        elif event.type==pygame.MOUSEMOTION:
           #pygame.draw.circle(Surface,color,pos圆心,radius半径,width边缘宽度)
            if event.pos[0]<p1[0] or event.pos[1]<p1[1] or event.pos[0]>p1[0]+f1_size*len(s1) or event.pos[1]>p1[1]+f1_size:
                p=event.pos

    end=time.perf_counter()   #结束计时
    back_color.r=255-f_color.r
    back_color.g=255-f_color.g
    back_color.b=255-f_color.b
    back_color.a=255-f_color.a
    screen.fill(back_color)  #填充背景颜色
    i=int(round((end-start),6)*1000)/1000
    if i-word_time>=int(round(1/n_word,3)*1000)/1000:    #考虑舍入误差
        n_word=n_words
        if j==1:
            s1=Read_file()
            f1 = pygame.freetype.Font("C://Windows//Fonts//Arial.ttf", 100)
        elif j==-1:
            s1=Read_chinese_file()
            f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc", 100)


        f_color.r=255
        f_color.g=255
        f_color.b=255
        f_color.a=255

        #f_color.r=Color_change(255)
        #f_color.g=Color_change(255)
        # f_color.r = Color_change(word_time%255)
        # f_color.g = Color_change( word_time*n_word*10%255 )
        # f_color.b = Color_change( n_word * 255 / 15)
        # f_color.a = Color_change(255-(i*100%150))
        word_time=i

    pygame.draw.circle(screen, f_color, p, 10, 3)  #绘制圆圈

    s2 = "Elapsed time: " + str(i) + " sec"
    s3 = "FPS:" + str(round(fclock.get_fps()))
    f1rech = f1.render_to(screen, p1,s1, fgcolor=f_color, size=f1_size)
    f2rech = f2.render_to(screen, p2, s2, fgcolor=f_color, size=f2_size)
    f3rech = f3.render_to(screen, p3, s3, fgcolor=f_color, size=f3_size)
    pygame.display.update()   #刷新屏幕
    fclock.tick(fps)   #控制帧率