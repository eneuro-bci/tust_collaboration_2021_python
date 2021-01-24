def func(list1, list2):
    list1.extend(list2)
    return list1


list1 = list(range(5))
list2 = list(range(5, 10))
# lst2 = ["a", "b", "c"]
print(func(list1, list2))
