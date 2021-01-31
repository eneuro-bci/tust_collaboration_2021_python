'''
最小开发框架
1，引入pygame,sys库
2，初始化设置（init（））
3，获取事件并逐步响应
4，刷新屏幕
'''
import pygame,sys
import randomword as randomword
#initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Word cycle")
#backpaper=pygame.image.load(r"backpicture1.png")
font = pygame.font.SysFont("arial", 16)#typeface

clock = pygame.time.Clock()#Create an object to help track time
first_time = pygame.time.get_ticks()#Gets the time in milliseconds

words = randomword.get_random_word()
show_word = pygame.USEREVENT + 1
pygame.time.set_timer(show_word, 1000)

#Get the time and respond step by step
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == show_word:
            words = randomword.get_random_word()

    last_time = pygame.time.get_ticks()  # Get the current program time

    time = (last_time - first_time) // 1000  # Calculate program time
    fps = int(clock.get_fps())

    screen.fill("black")  # output text content
    text_surface1 = font.render("Time:" + str(time)+' s', True, "red")
    screen.blit(text_surface1, (10, 10))
    text_surface2 = font.render("fps:" + str(fps)+' f/s', True, "red")
    screen.blit(text_surface2, (690, 10))   #Set position

    clock.tick(60)   #Limit game maximum frame rate
    w = font.render(str(words), True, 'red')   #Font and color
    screen.blit(w, (400, 300))   #Parameter meaning, image and location
    #Refresh screen
    pygame.display.update()
