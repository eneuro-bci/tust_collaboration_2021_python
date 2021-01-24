n = int (input("请输入数字n："))
print("1.计算1到n的和 2.计算1到n的乘积 ")
choose = int(input("您的选择是："))
if choose == 1:
    sum = 0
    for x in range(n+1):
        sum += x
    print(sum)
else:
    mul = 1
    for y in range(1,n+1):
        mul *= y
    print(mul)
