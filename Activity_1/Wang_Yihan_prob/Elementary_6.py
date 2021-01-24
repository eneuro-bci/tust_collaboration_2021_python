n=input()
m=int(n)
o=input("add10product10\n")
numbers=1
if o=='0':
    print(m*(m+1)/2)
elif o=='1':
    for number in range(1,m+1):
        numbers=number*numbers
    print(numbers)
else:
    print(Error)
