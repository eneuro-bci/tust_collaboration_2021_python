def func(list1, list2):
    list1.sort()
    list2.sort()
    list1.extend(list2)
    list1.sort()
    print(list1)


list1 = [9, 5, 23, 7.2, 3]
list2 = [654, 321, 8, 2, 44, 1]

func(list1, list2)
