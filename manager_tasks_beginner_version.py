input_task = input( "Введите категрию задачи:Работа,учеба,развлечение: ")
if input_task == "Работа":
    try:
        with open("Input_work.txt","w") as file:
            tasks = input( "Введите задачи через запятую: ").split(',') # ввод задач
            file.write('\n'.join(tasks)) # запись задач в файл
    except Exception :
           print( "Ошибка в открытии файла")
    try:
        with open("Input_work.txt","r") as file:
            tasks = file.read()
            
        with open("Output_work.txt","w") as file:
            file.write(tasks)  #Вывод задач в другой файл 
            print("Список задач сохранён в файл 'Output_work.txt'.")
    except Exception:
        print( "Неудалось прочитать или открыть документ")
     
         
            

elif input_task == "Учеба":
    try:
        with open("Input_study.txt","w") as file:
            tasks_2 = input( "Введите задачи через запятую: ").split(',') # ввод задач
            file.write('\n'.join(tasks_2)) # запись задач в файл
    except Exception:
        print( "Ошибка в открытии для записи файла")
    try:
        with open("Input_study.txt","r") as file:
            tasks_2 = file.read()
        with open("Output_study.txt","w") as file:
            file.write(tasks_2)    #Вывод задач в другой файл 
            print("Список задач сохранён в файл 'Output_study.txt'.")
    except Exception:
        print("Неудалось прочитать или открыть документ")
    

elif input_task == "Развлечение":
    try:
        with open("Input_entertaiment.txt","w") as file:
            tasks_3 = input( "Введите задачи через запятую: ").split(',')  # ввод задач
            file.write('\n'.join(tasks_3))  # запись задач в файл
    except Exception:
        print( "Ошибка в открытии для записи файла")

    try:
        with open("Input_entertaiment.txt","r") as file:
            tasks_3 = file.read()
            print("Список задач сохранён в файл 'Output_entertainment.txt'.")

        with open("Output_entertaiment.txt","w") as file:
            file.write(tasks_3)                       #Вывод задач в другой файл
    except Exception:
        print("Неудалось прочитать или открыть документ")
            
else:
    print("Категория задач указана неверно")


             
             
        

