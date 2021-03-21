n=input()
num=int(n)
a=input("Add and input 0, multiply and input 1\n")
numbers=1
if a=='0':
    print(num*(num+1)/2)
elif a=='1':
    for number in range(1,num+1):
        numbers=number*numbers
    print(numbers)
else:
    print(Error)
