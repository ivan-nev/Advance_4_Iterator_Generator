def factorial(number):
    # Валидация входного значения
    if not isinstance(number, int):
        raise TypeError("Число должно быть целым.")
    if number < 0:
        raise ValueError("Число должно быть неотрицательным.")
    # Расчет факториала
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

print(factorial((6)))

nested_list = [
    ['a', 'b',True,[77,33], 'c'],
    ['d', 'e', 'f', 'h'],
    [1, 2],'cv'
]

# print(any(isinstance(i, list) for i in nested_list))
temp_list =[]
while True:
    if any(isinstance(i, list) for i in nested_list):
        for i in nested_list:
            if isinstance(i,list):
                temp_list.extend(i)
            else:
                temp_list.append(i)
        nested_list = temp_list
        temp_list = []
    else: break
print (nested_list)





# #     l2 =[item for sublist in nested_list for item in sublist]
# # print (l2)
# def flat(list3):
#     l2 = []
#     for i in list3:
#         if isinstance(i,list):
#             flat(i)
#         l2.extend(i)
#     return l2
#
# s2 = flat(nested_list)
# print (s2)
#
# # s4= [3,67,4,False,[8,5,2]]
# # l4 = []
# # for i in s4:
# #     print (i)
# #     l4.append(i)
# # print(l4)