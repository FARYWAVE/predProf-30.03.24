import csv

monsters = {} # создаём словарь для записи максимальныъ значений

with open('monster_game.csv', encoding='utf-8-sig') as file: # открываем файл
    data = list(csv.DictReader(file, delimiter=','))
    for monster in data: # перебираем монстров и высчитываем силу
        if monster["opportunity"] == "регенерация":
            power = int(monster["health"]) * int(monster['probability']) / 100
        elif monster["opportunity"] == "дополнительный ход":
            power = int(monster['probability']) * (
                    int(monster["attack"]) + int(monster["protection"]) + int(monster["health"]) + int(
                monster["speed"])) / 100
        elif monster["opportunity"] == "усиление атаки":
            power = int(monster["attack"]) * int(monster['probability']) / 100

        try:
            if monsters[monster['opportunity']] < power: # записываем силу в словарь
                monsters[monster['opportunity']] = power
        except:
            monsters[monster['opportunity']] = power

with open('monster_opportunity.csv', 'w', newline='', # открываем файл для записи
          encoding='utf-8-sig') as new_file:
    writer = csv.DictWriter(new_file, delimiter=',',
                            fieldnames=['opportunity', 'power'])
    writer.writeheader()
    for i in monsters.keys(): # записываем результат
        opportunity = {}
        opportunity['opportunity'] = i
        opportunity['power'] = monsters[i]
        writer.writerow(opportunity)
