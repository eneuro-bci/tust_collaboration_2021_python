def func( a,b,n ):
    for i in range(n-1):
        a,b = b,a+b
        print (a)
    list(a)

a = 0
b = 1
n = 100
func(a,b,n)