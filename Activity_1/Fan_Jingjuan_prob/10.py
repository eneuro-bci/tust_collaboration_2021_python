year = int(input("输入当前年份"))
x=0
for i in range(year,9999):
     if i%4==0:
          if i%100!=0 or i%400==0:
               print(i)
               x+=1
     if x>=20:
          break
