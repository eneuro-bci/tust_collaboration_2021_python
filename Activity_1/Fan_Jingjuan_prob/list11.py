def func(list1,list2):
     list1.extend(list2)
     list1.sort()
     print(list1)
list1=[0,2,4,6,8]
list2=[1,3,5,7,9]
func(list1,list2)
