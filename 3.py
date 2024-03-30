import csv
with open('monster_game.csv', encoding='utf-8-sig') as file: # открываем файл
    data = list(csv.reader(file, delimiter=','))
    headings = data.pop(0)
    while True:  # запускаем бесконечный цикл
        playerPower = input() # считываем данные
        if playerPower == "хватит": # прирываемся при вводе стоп-слова
            break
        playerPower = int(playerPower)
        counter = 0 # счетчик монстров

        for monster in data: # перебираем мостров и проверяем условие
            if monster[5] != '0' and int(monster[5]) < playerPower:
                counter += 1
        if counter == 0: # вывод
            print('Вы очень слабы. Сходите и наберитесь опыта!”. ')
        else:
            print(f"Вы сможете победить: {counter} монстров")