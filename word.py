
from py_random_words import RandomWords
import random

def Read_file():
    rnd_word=RandomWords()
    return rnd_word.get_word()  #返回单词
def Read_chinese_file():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)

def Color_change(a):
    return 0 if a < 0 else (255 if a > 255 else int(a))




