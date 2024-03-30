import csv
clssCount = {} # создаем словари для записи количества монстров каждого клсса и суммы атаки каждого класса
clssSumm = {}  # для дальнейшего вычесления среднего арифметического


with open('monster_game.csv', encoding='utf-8-sig') as file: # открываем файл
    data = list(csv.reader(file, delimiter=','))
    headings = data.pop(0)
    for monster in data: # перебираем монстров и заполняем словари
        clss = monster[0].split()[1]
        try:
            clssCount[clss] += 1
            clssSumm[clss] += int(monster[3])
        except:
            clssCount[clss] = 1
            clssSumm[clss] = int(monster[3])

for i in clssCount.keys(): # выводим данные, вычисляя среднее арифметическое
    print(f"{str(clssCount[i])} монстров класса {i}, средняя сила атаки {str(clssSumm[i] / clssCount[i])}")