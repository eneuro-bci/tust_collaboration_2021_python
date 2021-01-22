#需要调用的函数
def fun(n):
    if n<=1:
        if n==0 or n==1:
            return 1
        else:
            print('N cannot be less than 0')
    else:
        return n*fun(n-1)

num=int(input('Please enter a number：'))
print('1:Calculation and    2：Calculate multiply')
nums=int(input('Please select the appropriate operation'))
if nums==1:
    sum=0
    for i in range(num+1):
        sum+=i
    print('sum：',sum)
elif nums==2:
    sum=fun(num)
    print(sum)

