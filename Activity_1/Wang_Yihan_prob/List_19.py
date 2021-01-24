def stamp(ch):
    number=[]
    for num in ch:
        number.append(len(num))
    Max=max(number)
    for n2 in range(0,len(number)+2):
        
        
        if n2==0 or n2==len(number)+1:
            for n1 in range(0,Max+4):
                print("*",end="")
            print()
        else:
            print("* ",end="")
            print(ch[n2-1],end="")
            for n3 in range(0,Max-number[n2-1]):
                print(" ",end="")
            print(" *")
ch=['Hello','world','in','a','frame']
stamp(ch)
