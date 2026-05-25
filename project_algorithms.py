"""
 система управления пользователями!

 создаю программу, где можно:
 Добавлять пользователей (имя + ID).
 Быстро находить пользователя по ID (бинарный поиск).
 Сортировать пользователей (по ID или имени).
 Удалять пользователей.


---

Что использовал?

Бинарный поиск – для быстрого поиска пользователя по ID.

Рекурсия – для поиска минимума или сортировки.

Быстрая сортировка – для сортировки пользователей.
"""
import sys
users = [
    (101, "Алиса"),
    (205, "Борис"),
    (150, "Виктор"),
    (312, "Галина"),
    (250, "Дмитрий"),
    (400, "Екатерина"),
    (120, "Женя"),
    (330, "Иван"),
    (275, "Ксения"),
    (500, "Леонид")
]

def quick_sort(users):
    if len(users) < 2:
        return users
    else:
        piv = users[0]
        less = [i for i in users[1:] if i <= piv]
        gr = [i for i in users[1:] if i > piv]
        return quick_sort(less) + [piv] + quick_sort(gr)
sort_users = quick_sort(users)



def binary_search(users,value):
    low = 0
    high = len(users) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = users[mid][0]
        if guess == value:
            return users[mid]
        elif guess > value:
            high = mid - 1
        else:
            low = mid + 1
    return "Пользоватаель с таким Id отсутсвует"

while True:
    print("Выберите действие которое хотите выполнить:")
    print("1 - Добавить пользователя")
    print("2 - Удалить пользователя")
    print("3 - Найти пользователя")
    print("4 - Вывести список пользователей")
    print("5 - Выйти")
    action = int(input("Введите номер действия: ")) 
    if action == 1:
        add_user_id = int(input("Введие ID пользователя: "))
        add_user_name = input("Введите имя нового пользователя: ")
        users.append((add_user_id,add_user_name))
        users = quick_sort(users)
        for user in users:
            print(user[0], "-",user[1])
    elif action == 2:
        delete_user_id = int(input("Введите ID пользователя которого хотите удалить: "))
        users = [user for user in users if user[0] != delete_user_id]
        for user in users:
            print(user[0],"-",user[1])
    elif action == 3:
        value = int(input("Введите ID пользовтаеля которого хотите найти: "))
        sorted_users = binary_search(users,value)
        print(sorted_users)

    elif action == 4:
        for key,usr in users:
            print(key,usr)
    elif action == 5:
        sys.exit()
    else:
        print("Вы ввели несуществующую команду")


       


                           
