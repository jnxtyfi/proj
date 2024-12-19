print("Задача 1:")
a = input('Введите число: ')

for i in range(1, int(a) + 1):
	print(i)

print("Задача 2:")

first = input('Введите первое число: ')
second = input('Введите второе число: ')

print("Большее число: " + str(max(int(first), int(second))))