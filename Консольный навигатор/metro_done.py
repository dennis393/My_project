from collections import deque
def print_countries_capital():
    print("В настоящее время доступны лишь несколько карт, также в разработке находятся карты стран СНГ, \nевропейские метрополитены появятся позже")
    print()
    print()
    countries_capital = {'Азербайджан' :["Баку"],
                         'Армения' :["Ереван"],
                         'Беларусь' :["Минск"],
                         'Казахстан' :["Алматы"],
                         'Россия' :["Москва", "Санкт - Петербург",
                                    "Нижний Новгород", "Самара",
                                    "Екатеринбург", "Казань"],
                         'Узбекистан' :["Ташкент"],
                         'Украина' :["Киев", "Харьков", "Днепр"]
                         }
    for country in sorted(countries_capital.keys()):
        cities = ', '.join(countries_capital[country])
        print("{}: {}".format(country, cities))
       
print_countries_capital()    

def print_moscow_metro():
    return False

def print_minsk_metro():
    return False #если карта не готова


#В функции ничего не изменять,вывод ровный несмотря на то,что пробелы в коде стоят неровно 
def print_tashkent_metro(): 
    print("                                                    Turkiston • ")
    print("                                                               \\")
    print("                                                      Yunusobod •")
    print("                                                                 \\")
    print("                                                       Shahriston •")
    print("                                                                   \\")
    print("                                                           Bodomzor •          • Buyuk Ipak Yoli") 
    print("                                                                     \\         |")
    print("                                                                Minor •        • Pushkin")   
    print("                                                                       \\\      |")
    print("                                                        Abdulla Qodiriy •      • Hamid Olimjon")
    print("                                                                         \\   /")
    print("                                                                          ⟲ • Amir Temur xiyoboni⟲ ― • Yunus Rajabiy")
    print("                                                                           /                        |")
    print("                                                                          • Mustakillik maydoni     | ")
    print("                                                                         /                          ⟲ Ming Orik      ")
    print("   •Beruniy ⇄ •Tinchlik ⇄  •Chorsu ⇄ •G'ofur G'ulom ⇄ •Alisher Navoiy ⟲Paxtakor ⇄ •Ozbekiston ⇄  • Oybek  ⇄  • Toshkent ⇄  • Mashinasozlar  ⇄   • Dostlik") 
    print("                                                                        |                                                                            |")
    print("                                                                        • Xalqlar Do‘stligi                                                          • Texnopark")
    print("                                                                        |                                                                            | ")
    print("                                                                        • Milliy bog‘                                                                • Yashnobod ")
    print("                                                                        |                                                                            | ")
    print("                                                                        • Novza                                                                      • Tuzel ")
    print("                                                                        |                                                                           / ")
    print("                                                                        • Mirzo Ulug‘bek                                                           • Olmos ")
    print("                                                                        |                                                                         / ")
    print("                                                                        • Chilonzor                                                              • Rohat  ")
    print("                                                                        |                                                                       / ")
    print("                                                                        • Olmazor                                                              • Yangiobod   ")
    print("                                                                        |                                                                     / ")
    print("                                                                        • Choshtepa                                                          •Qoyliq  ")
    print("                                                                        |                                                                   /  ")
    print("                                                                        • O‘zgarish                                                        •  Matonat ")
    print("                                                                        |                                                                 / ")
    print("                                                                        • Sergeli                                                        • Qiyot  ")
    print("                                                                        |                                                               / ")
    print("                                                                        • Yangihayot                                                   • Tolariq  ")
    print("                                                                        |                                                             / ")
    print("                                                                        • Chinor ― Qipchok • ―  Turon • ―  • Qiruvchilar ― • Xonobod • ")
    return True #если карта готова


LINE_NAMES = {
    'Red': 'Чиланзарская линия',
    'Blue': 'Узбекистанская линия',
    'Green': 'Юнусабадская линия',
    'Transfer': 'Пересадка'
}
metro_graph = {
    # Зелёная ветка
    'Turkiston': [('Yunusobod', 'Green')],
    'Yunusobod': [('Turkiston', 'Green'), ('Shahriston', 'Green')],
    'Shahriston': [('Yunusobod', 'Green'), ('Bodomzor', 'Green')],
    'Bodomzor': [('Shahriston', 'Green'), ('Minor', 'Green')],
    'Minor': [('Bodomzor', 'Green'), ('Abdulla Qodiriy', 'Green')],
    'Abdulla Qodiriy': [('Minor', 'Green'), ('Amir Temur xiyoboni-G', 'Green')],
    'Amir Temur xiyoboni-G': [
        ('Abdulla Qodiriy', 'Green'),
        ('Yunus Rajabiy', 'Green'),
        ('Amir Temur xiyoboni-R', 'Red') # Пересадка
    ],
    'Yunus Rajabiy': [('Amir Temur xiyoboni-G', 'Green'), ('Ming Orik-G', 'Green')],
    'Ming Orik-G': [('Yunus Rajabiy', 'Green'), ('Ming Orik-B', 'Blue')],
    
    # Красная ветка
    'Amir Temur xiyoboni-R': [
        ('Amir Temur xiyoboni-G', 'Green'), # Пересадка
        ('Mustakillik maydoni', 'Red'),
        ('Hamid Olimjon', 'Red')
    ],
    'Mustakillik maydoni': [('Amir Temur xiyoboni-R', 'Red'), ('Paxtakor-R', 'Red')],
    'Paxtakor-R': [
        ('Mustakillik maydoni', 'Red'),
        ("Xalqlar Do'stligi", 'Red'),
        ('Paxtakor-B', 'Blue') # Пересадка на синюю
    ],
    "Xalqlar Do'stligi": [('Paxtakor-R', 'Red'), ("Milliy bog'", 'Red')],
    "Milliy bog'": [("Xalqlar Do'stligi", 'Red'), ('Novza', 'Red')],
    'Novza': [("Milliy bog'", 'Red'), ("Mirzo Ulug'bek", 'Red')],
    "Mirzo Ulug'bek": [('Novza', 'Red'), ('Chilonzor', 'Red')],
    'Chilonzor': [("Mirzo Ulug'bek", 'Red'), ('Olmazor', 'Red')],
    'Olmazor': [('Chilonzor', 'Red'), ('Choshtepa', 'Red')],
    'Choshtepa': [('Olmazor', 'Red'), ("O'zgarish", 'Red')],
    "O'zgarish": [('Choshtepa', 'Red'), ('Sergeli', 'Red')],
    'Sergeli': [("O'zgarish", 'Red'), ('Yangihayot', 'Red')],
    'Yangihayot': [('Sergeli', 'Red'), ('Chinor', 'Red')],
    'Chinor': [('Yangihayot', 'Red')],
    'Hamid Olimjon': [('Amir Temur xiyoboni-R', 'Red'), ('Pushkin', 'Red')],
    'Pushkin': [('Hamid Olimjon', 'Red'), ('Buyuk Ipak Yoli', 'Red')],
    'Buyuk Ipak Yoli': [('Pushkin', 'Red')],
    
    # Синяя ветка
    'Dostlik': [('Mashinasozlar', 'Blue')],
    'Mashinasozlar': [('Toshkent-B', 'Blue'), ('Dostlik', 'Blue')],
    'Toshkent-B': [('Oybek', 'Blue'), ('Mashinasozlar', 'Blue'), ('Ming Orik-B', 'Blue')],
    'Oybek': [('Toshkent-B', 'Blue'), ('Ozbekiston', 'Blue')],
    'Ozbekiston': [('Oybek', 'Blue'), ('Paxtakor-B', 'Blue')],
    'Paxtakor-B': [
        ('Ozbekiston', 'Blue'),
        ("Alisher Navoiy", 'Blue'),
        ('Paxtakor-R', 'Red') # Пересадка на красную
    ],
    "Alisher Navoiy": [('Paxtakor-B', 'Blue'), ("G'ofur G'ulom", 'Blue')],
    "G'ofur G'ulom": [("Alisher Navoiy", 'Blue'), ('Chorsu', 'Blue')],
    'Chorsu': [("G'ofur G'ulom", 'Blue'), ('Tinchlik', 'Blue')],
    'Tinchlik': [('Chorsu', 'Blue'), ('Beruniy', 'Blue')],
    'Beruniy': [('Tinchlik', 'Blue')],
    'Ming Orik-B': [('Toshkent-B', 'Blue'), ('Ming Orik-G', 'Green')],
}

metro_maps = {'ташкент' :print_tashkent_metro,#сюда поставить граф Ташкента и так для всех
              'москва' :print_moscow_metro,
              'минск' :print_minsk_metro
              }

   
print()


def metro_bfs(metro_graph, start, end): #Функция для нахождения пути станций
    if start not in metro_graph:
        print("Станция",start, "не найдена")
        return None
    if end not in metro_graph:
        print("Станция", end, "не найдена")
        return None
    if start == end:
        print("Вы находитесь на нужной станции")
        return None
 
    queue = deque()
    visited = set()

    start_line = metro_graph[start][0][1]
    queue.append((start, start_line, [(start, start_line)]))
    visited.add((start, start_line))
    while queue:
        curr_station, curr_line, path = queue.popleft()
        for neigh, line in metro_graph[curr_station]:
            if neigh == end:
                return path + [(neigh, line)]
            if (neigh, line) not in visited:
                visited.add((neigh, line))
                queue.append((neigh, line, path + [(neigh, line)]))
    return None


def print_route(route):
    if not route:
        print("Маршрут не найден")
        return 
    current_line = route[0][1]
    segment_start = 0

    for i in range(len(route)):
        station, line = route[i]
        
        if line != current_line or i == len(route) - 1:
            segment_end = i if line != current_line else i + 1

            print("Линия:", LINE_NAMES.get(current_line, current_line))

            for j in range(segment_start, segment_end):
                s, l = route[j]
                if j == segment_start:
                    if segment_start == 0:
                        print("   |-", s, "(посадка)")
                    else:
                        print("   |-", s)
                elif j == segment_end - 1:
                    if i == len(route) - 1:
                        print("   |-", s, "(выход)")
                    else:
                        print("   |-", s)
                else:
                    print("   |-", s)

            # Проверка "Если это не последняя станция и линия изменилась"
            if i < len(route) - 1 and line != current_line:
                print("\n   Пересадка")
                print("   Перейдите на линию:", LINE_NAMES.get(line, line),"\n")

                current_line = line
                segment_start = i

  
    print("Всего станций:", len(route))

    # Подсчёт пересадок
    transfers = 0
    prev_line = route[0][1]
    for _, line in route[1:]:
        if line != prev_line:
            transfers += 1
            prev_line = line

    print("Количество пересадок:", transfers)
print_countries_capital()
print()
city = input("Введите город: ").lower()
if city in metro_maps:
    ready_map = metro_maps[city]() #вернет True или False
    if ready_map:
        start = input("Откуда: ")
        end = input("Куда: ")
        route = metro_bfs(metro_graph, start, end)
        if route:
            print_route(route)
    else:
        print("Путь построить нельзя,карта в разработке")
    
else:
    print("Карта для этого города не найдена")


