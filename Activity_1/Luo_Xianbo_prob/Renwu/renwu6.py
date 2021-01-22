def fun(lst1,lst2):
    new_lst = []
    print('First list', lst1)
    print('Second list', lst2)
    for item in lst1:
        new_lst.append(item)
    for item in lst2:
        new_lst.append(item)
    print('Spliced list', new_lst)
    new_lst.sort()
    print(new_lst)

lst1=[1,3,5,7,9]
lst2=[2,4,6,8]
fun(lst1,lst2)