def odd_number(number):
    numbers=list(range(1,len(number)+1,2))
    return numbers

number=[1,2,3,4,5]
numbers=odd_number(number)

print(numbers)
