# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def degree(a,b):
    if b == 1:
        return a
    if b !=1:
        return (a**b)


a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
print(f'целая степень числа а = {degree(a,b)}')






