years=input("输入开始年份\n")
num=0
year=int(years)
while num<20:
    if year%4==0 and year%100!=0:
        print(year)
        num+=1
        year+=1
    elif year%400==0:
        print(year)
        num+=1
        year+=1
    else:
        year+=1
