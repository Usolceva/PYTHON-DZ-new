# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5 1 2 3 4 5
#     6
#     -> 5

import random

number = int(input('Введите количество элементов: '))
my_list = []
for _ in range(number):
 my_list.append(random.randint(1,30))
print(my_list)

x = int(input('Введите искомое число х: '))

#for i in range(len(my_list)):
if my_list.count(x) == 0:
  nearest = my_list[0]
  for num in my_list:
   if abs(x - num) < abs(x - nearest):
    nearest = num
    print(f'самый близкий по величине элемент к заданному числу {x}: {nearest}')


4542