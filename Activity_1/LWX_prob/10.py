n = int(input("请输入一个年份：\n"))
print("未来二十年内的闰年有：")
for i in range(n, n + 21):
    if (i % 4 == 0 and i % 100 != 0) or (i % 100 == 0 and i % 400 == 0):
        print(str(i) + '\t', end='')


# Problem: Write a program that prints the next 20 leap years
# Note: you are missing some years in here
