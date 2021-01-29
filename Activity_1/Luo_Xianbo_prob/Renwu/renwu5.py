# 拼接
def fun(lst1, lst2):
    new_lst = []
    print('First list', lst1)
    print('Second list', lst2)
    for item in lst1:
        new_lst.append(item)
    for item in lst2:
        new_lst.append(item)
    print('Spliced list', new_lst)


# Also add the function call for testing purposes
# fun(lst1=[1, 2, 3], lst2=["a", "b", "c"])
