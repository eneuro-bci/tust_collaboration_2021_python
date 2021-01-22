n = int (input("请输入一个整数n："))
print("请选择： \n 1.输出1-n的累加和 \n 2.输出1-n的乘积 \n")
choose = int(input("您的选择是："))
if choose == 1:
    sum = 0
    for i in range(n+1):
        sum += i
    print("和为：" + str(sum))
else:
    mul = 1
    for j in range(1,n+1):
        mul *= j
    print("乘积为：" + str(mul))