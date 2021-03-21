# n = int(input("请输入一个年份：\n"))
# print("未来二十年内的闰年有：")
# for i in range(n, n + 21):
#     if (i % 4 == 0 and i % 100 != 0) or (i % 100 == 0 and i % 400 == 0):
#         print(str(i) + '\t', end='')


# Problem: Write a program that prints the next 20 leap years
# Note: you are missing some years in here

# New version given by LWX
n = int(input("请输入一个年份：\n"))
print("未来二十年内的闰年有：")
count = 0
none = True
while none:
    if count < 20:
        if (n % 4 == 0 and n % 100 != 0) or (n % 100 == 0 and n % 400 == 0):
            print(str(n) + '\t', end='')
            count += 1
            n += 1
        else:
            n += 1
    else:
        none = False
