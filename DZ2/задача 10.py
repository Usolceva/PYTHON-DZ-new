#10. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
import random

# coins = int(input('Введите количество монет: '))
# my_coins = [random.randint(0,1) for i in range(coins)]
# print(my_coins)
# coins_0 = 0
# coins_1 = 1
# for i in range(coins):
#     if  my_coins[i] == 0:
#         coins_0 += 1
#     else:
#          my_coins[i] == 1
#          coins_1 += 1
# if coins_0 > coins_1:
#      print( 'надо перевернуть единицы')
# elif coins_0 == coins_1:
#     print( 'их одинаково, бз разницы что перевернуть')
# else:
#     print( 'надо перевернуть нули')


# #        2 РЕШЕНИЕ
# coins = int(input('Введите количество монет: '))
# my_coins = [random.randint(0,1) for i in range(coins)]
# print(*my_coins) # * УБИРАЕТ СКОБКИ И ЗАПЯТИЫЕ В МАССИВЕ

# print('переверни единички' if my_coins.count(1) < coins //2 else 'переверни нолики') # работает криво, просто для просмотра как можно сократить в одну строку


#  3 РЕШЕНИЕ:
coins = int(input('Введите количество монет: '))
my_coins = [random.randint(0,1) for i in range(coins)]
print(*my_coins)

if my_coins.count(1) < my_coins.count(0):
    print(f'переверни единички! их {my_coins.count(1)}')
elif my_coins.count(1) > my_coins.count(0):
    print(f'переверни нолики! их {my_coins.count(0)}')
else:
    print(f'переверни что хочешь! их {my_coins.count(1)}')



