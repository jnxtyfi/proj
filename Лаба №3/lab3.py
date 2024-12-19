print('Задание №1')
with open('txt.txt', 'r') as file:
    content = file.read()
print(content)
with open('txt.txt', 'r') as file:
    for line in file:
    	print(line, "\n")

print("Задание №2")

with open('user_input.txt', 'r') as f:
    cont = f.read()
cont = cont + " " + input("Введите текст: ")
with open("user_input.txt", "w") as f:
    f.write(cont)

print("Задание 3")
try:
    with open('1111.txt', 'r') as file:
        content = file.read()
    print(content)
    with open('111.txt', 'r') as file:
        for line in file:
            print(line, "\n")
except FileNotFoundError:
    print("Файла нет")