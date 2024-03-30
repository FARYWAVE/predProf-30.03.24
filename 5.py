import csv

with open('monster_game.csv', encoding='utf-8-sig') as file: # открываем файл
    data = list(csv.reader(file, delimiter=','))
    headings = data.pop(0)
    table = {} # создаём таблицу
    for monster in data: # перебираем мостров и заполняем таблицу
        hashCode = monster[0] + monster[1] + monster[2] # создаём хэш-код
        table[hashCode] = monster[1]

    k = 0 # счетчик количества выведенных результатов
    for i in table.keys(): # выводим первые 10
        print(i + " - " + table[i])
        k += 1
        if k == 10: # останавливаемся если вывели 10 результатов
            break
