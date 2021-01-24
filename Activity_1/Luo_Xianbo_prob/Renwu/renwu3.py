print('It is 2021,These are the leap years in the next 20 years')
firstyear = int(input('Enter the current year '))
sum = 0
for years in range(firstyear, 9999):
    if years % 4 == 0:
        if years % 100 != 0 or years % 400 == 0:
            print(years, 'is leap year')
            sum += 1
    if sum >= 20:
        break
