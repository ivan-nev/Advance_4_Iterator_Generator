import datetime

def my_range(start, end):
    while start < end:
        yield start    # yield попадает в item цикла for
        start +=1

def my_date_range(start, end):
    while start < end:
        yield start    # yield попадает в item цикла for
        start += datetime.timedelta(days=1)

for item in my_range(1,10):
    print(item)

for item in my_date_range(datetime.date(2022, 9, 25), datetime.date(2022, 10, 3)):
    print(item)

num = [1, 2, 3, 4, 5, 6]
sq_num = [i**2 for i in range(0,100) if i % 10 == 0]  # получили сразу список
sq_num2 = (i**2 for i in num if i % 2 == 0)  # получили генератор списка
print(sq_num)
print(sq_num2)
for item in sq_num2:
    print(item)
