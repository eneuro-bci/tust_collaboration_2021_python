import pygame,sys
import randomword as randomword
import random

pygame.init()
window_WIDTH = 800
window_HEIGHT = 600
window = pygame.display.set_mode((window_WIDTH, window_HEIGHT))
pygame.display.set_caption("Word cycle")

word_size = 16
font = pygame.font.SysFont("arial", word_size)  # typeface
font1 = pygame.font.SysFont("arial", 16)

clock = pygame.time.Clock()  # Create an object to help track time
first_time = pygame.time.get_ticks()  # Gets the time in milliseconds

words = randomword.get_random_word()
show_word = pygame.USEREVENT + 1
pygame.time.set_timer(show_word, 1000)  # 每1秒替换一个单词

# Get the time and respond step by step
# 字的位置参数
word_x, word_y = 400, 300

while True:
    for event in pygame.event.get():
        # 第一个需求：NUMPAD控制字的位置，8，4，2，6控制上下左右，5 字的位置到中心位置，0 分配一个随机位置
        if event.type == pygame.KEYDOWN:
            print(event.key)
            # Move up
            if event.key == 1073741920:
                if word_y <= 0:
                    word_y = word_y
                elif word_y > 0:
                    word_y = word_y - 10
            # Move down
            elif event.key == 1073741914:
                if word_y >= window_HEIGHT:
                    word_y = window_HEIGHT
                elif word_y < window_HEIGHT:
                    word_y = word_y + 10
            # Move left
            elif event.key == 1073741916:
                if word_x <= 0:
                    word_x = word_x
                elif word_x > 0:
                    word_x = word_x - 10
            # Move right
            elif event.key == 1073741918:
                if word_x < window_WIDTH:
                    word_x = word_x + 10
                elif word_x >= window_WIDTH:
                    word_x = word_x
            # Back to the center
            elif event.key == 1073741917:
                word_y = window_HEIGHT/2
                word_x = window_WIDTH/2
            # Random in one place
            elif event.key == 1073741922:
                word_y = random.randint(50, 600)
                word_x = random.randint(50, 600)
        # 第二个需求：使用上下方向键调整字的大小
            elif event.key == 1073741906:
                # 将字体放大
                word_size = word_size + 10
            elif event.key == 1073741905:
                # 将字体缩小
                word_size = word_size - 10
            font = pygame.font.SysFont("arial", word_size)

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == show_word:
            words = randomword.get_random_word()
    last_time = pygame.time.get_ticks()  # Get the current program time
    time = (last_time - first_time) // 1000  # Calculate program time
    fps = int(clock.get_fps())
    # 显示位置和fps显示位置
    window.fill("black")  # output text content
    text_surface1 = font1.render("Time:" + str(time)+' s', True, "red")
    window.blit(text_surface1, (10, 10))
    text_surface2 = font1.render("fps:" + str(fps)+' f/s', True, "red")
    window.blit(text_surface2, (690, 10))   # Set position
    # 单词显示位置
    clock.tick(60)   # Limit game maximum frame rate
    w = font.render(str(words), True, 'red')   # Font and color
    window.blit(w, (word_x, word_y))   # Parameter meaning, image and location
    # Refresh screen
    pygame.display.update()
