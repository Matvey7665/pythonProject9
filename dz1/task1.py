import math

summa = int(input('Введите сумму чисел'))
pr = int(input("Введите произведение чисел"))
D = summa * summa - 4 * pr
a = (summa - math.sqrt(D)) / 2
b = (summa + math.sqrt(D)) / 2
print(a)
print(b)
