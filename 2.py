import csv
with open('monster_game.csv', encoding='utf-8-sig') as file: # открываем файл
    data = list(csv.reader(file, delimiter=','))
    headings = data.pop(0)
    for i in range(1, len(data)): # сортируем вставками по способности
        x = data[i]
        j = i
        while j > 0 and data[j - 1][1] < x[1]:
            data[j] = data[j - 1]
            j -= 1
        data[j] = x

    # выводим топ 3
    for i in range(3):
        monster = data[i]
        print(f"{monster[0]} имеет возможность: {monster[1]}, вероятность использования возможности равна {monster[2]}")
