def fun():
    item1 = 1
    item2 = 1
    item = 1
    while item < 100:
        print(item)
        item = item1 + item2
        item1, item2 = item2, item


print(fun())
