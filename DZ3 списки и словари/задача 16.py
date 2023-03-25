# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5  1 2 3 4 5
#     3
#     -> 1
import random

number = int(input('Введите количество элементов: '))
my_list = []
for _ in range(number):
 my_list.append(random.randint(1,10))
print(my_list)

x = int(input('Введите искомое число х: '))
count = 0
for i in range(len(my_list)):
 if (x == my_list[i]):
  count =+1
  print(count, end=' ')
