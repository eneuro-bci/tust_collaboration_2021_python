def Fi(n):
    F1=1
    F2=1
    if n==1 or n==2:
        print(1)
        return
    for n1 in range(3,n+1):
        F3=F1+F2
        F1=F2
        F2=F3
    print(F3)
Fi(100)
