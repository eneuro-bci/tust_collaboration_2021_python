print("九九乘法表：\n")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + "X" + str(i) + "=" + str(i * j) + "\t", end='')
    print(" ")
