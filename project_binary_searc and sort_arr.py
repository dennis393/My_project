
product = int(input("Введите колличество товаров,максимальное кол - во 10: "))
if product > 10:
    print("Вы ввели большее кол-во товара")
    exit()

products = [
    ("Молоко", 90),
    ("Хлеб", 50),
    ("Мясо", 250),
    ("Яблоки", 120),
    ("Рыба", 300),
    ("Картофель", 40),
    ("Сыр", 200),
    ("Чай", 75),
    ("Шоколад", 150),
    ("Йогурт", 110)
    ]
#Сортировка товаров по возрастанию в цене
def selection_search(products):
    val_product = len(products)
    for i in range(val_product):
        min_val = i
        for j in range(i+1,val_product):
            if products[j][1] < products[min_val][1]:
                min_val = j
        if min_val != i:
            products[i],products[min_val] = products[min_val],products[i]
    return products
sorted_products = selection_search(products)
for i in range(min(product,len(sorted_products))):
    print(sorted_products[i])

#Поиск по цене в каталоге при помощи бинарного поиска
def binary_search(products,val):
    low = 0
    high = len(products) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = products[mid][1]
        if guess == val:
            return products[mid]
        if guess > val:
            high = mid - 1
        else:
            low = mid + 1
    return "Такой цены нет в каталоге"
val = int(input("Введите цену для товара,который хотите найти: "))
sorted_products_bin = binary_search(sorted_products,val)
print(sorted_products_bin)

        

    

 




