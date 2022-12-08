# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:

#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# from random import randint


# def list(n):
#     list = []
#     for i in range(n):
#         list.append(randint(1, n))
#     return list
# n = int(input('Введите значение N: '))
# numbers = list(n)
# # print(list(n))
# s = 0
# for i in range(len(numbers)):
#     # if i % 2 == 1:
#         # print(i)
#         s+= len(numbers)

# print(f"{numbers} -> сумма элементов на нечётных позициях: {s}")

number = int(input('Введите размер списка '))
list = []
sum = 0
for i in range(number):
    list_number = int(input(f'Введите число {i+1} '))
    list.append(list_number)
    if i % 2 != 0:
        sum += list[i]


print(list)
print(f'Сумма нечетных чисел равна {sum}')

