#Калькулятор который вычисляет факториал и сумму цифр числа с помощью рекурсий
print("Выберите действие:")
print("1 - Найти факториал числа")
print("2 - Найти сумму цифр числа")
action = int(input("Выбор действия: "))
print("Ваш выбор: ",action)
num = int(input("Введите число: "))

#рекурсивная функция для фактоиала
def func_rec(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * func_rec(num - 1)

#Рекурсивная функция для вывода суммы числа
def sum_digits(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sum_digits(num//10)

if action == 1:
    print("Факториал введеного числа равен: ",func_rec(num))
elif action == 2:
    print("Сумма цифр введеного числа равна: ",sum_digits(num))
else:
    print("Введены некорретные данные")
