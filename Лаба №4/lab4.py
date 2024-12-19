from math import sqrt
from datetime import datetime
import pocket

print("\n\n\n Задание 1 \n")
a = input("Введите число: ")
try:
	print("Квадратный корень этого числа равен " + str(sqrt(int(a))))
except ValueError:
	print("И чё ты ввёл?")
print("\nМоя дата рождения (Год-месяц-число): " + str(datetime(2006, 6, 8)))

print("\n\n\n Задание 2 \n")

x = input("Введите число/строку: ")
print("Ваше число/строка в развёрнутом виде: " + str(pocket.rev(x)))

print("\n\n\n Задание 3 \n")

x = input("Введите первое число: ")
y = input("Введите второе число: ")

print(pocket.sum(x, y))

s = input("Введите строку: ")
print(pocket.rev(s))

a = input("Введите число: ")
b = input("Введите количество битов сдвига: ")
c = input('Введите направление сдвига ("l" - левый, "r" - правый): ')
print(pocket.sdv(a, b, c))