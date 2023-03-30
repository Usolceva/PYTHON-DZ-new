
# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. 
# не меньше заданного минимума и не больше заданного максимума)

import random
my_list = [random.randint(1,100) for _ in range(1,10)]
print(my_list)
mini = int(input('Введите минимальный элемент: '))
maxi = int(input('Введите максимальный элемент: '))
for i in range(len(my_list)):
    if mini <= my_list[i] <= maxi:
     print(i)