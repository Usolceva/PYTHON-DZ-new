
# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k
# долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Примеры:
# Примечание: каждое считывание производится с новой строки
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input('введите n долек: '))
m = int(input('введите m долек: '))
k = int(input('введите k долек: '))
if k < n*m and (k % n == 0 or k % m == 0):
    print('yes')
else:
    print('no')