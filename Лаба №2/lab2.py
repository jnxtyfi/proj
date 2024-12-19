"""print("Задание №1")
def greet(name):
	if len(name) < 3:
		return "Некорректно"
	return "Добро пожаловать, " + str(name)


a = input("Введите своё имя: ")
print(str(greet(a)))



def sqr(number):
	return int(number) ** 2

a = input("Введите число: ")
print("Квадрат этого числа: " + str(sqr(a)))



def max_of_two(x, y):
	return max(int(x), int(y))

x = input("Введите первое число: ")
y = input("Введите второе число: ")
print("Большее из чисел - " + str(max_of_two(x, y)))


"""


print("Задание №2")
def describe_person(name, age=30): 
	return "Вас зовут " + name + ", и вам " + age + " лет."

n = input("Ваше имя? ")
a = int(input("Сколько вам лет? "))
print(describe_person(n, a))



"""def is_prime(x):
	for i in range(1, int(x)):
		if int(x) % i == 0 and i != 1 and i != x:
			return "Число " + x + " не простое."
	return "Число " + x + " простое!"

x = input("Введите число: ")
print(is_prime(x))"""
			




