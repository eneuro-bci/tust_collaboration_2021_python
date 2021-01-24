def merge_sort(a,b):

    for n1 in range(0,len(a)):
        for n2 in range(0,len(b)):
            if a[n1]<b[n2]:
                b.insert(n2,a[n1])
                break
    print(b)

a=[3,5,7,9]
b=[4,6,8,10]
merge_sort(a,b)
