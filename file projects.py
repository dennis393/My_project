import random
with open('main.txt','w',encoding = 'utf-8') as f:
    symbol_for_password = "qwertyuiop[];lkjhgfdsazxcvbnm,./!@#$%^&*()_+'"
    f.write(symbol_for_password)

with open('main.txt','r',encoding = 'utf-8') as f:
    symbols_for_password = list(f.read())
    done_password = random.shuffle(symbols_for_password)
    done_password = ''.join(symbols_for_password[:14])

with open('done.txt','w',encoding = 'utf-8') as f:
          f.write(done_password)
          print("Ваш пароль сохранен в формате txt,проверьте папку 'Проекты'") 
