import myLib
myLib.vyvodPolya(myLib.vidimost_polya)
game = True
myLib.mins()
myLib.prov()
while game:
    while True:
        stroka = int(input("Введите номер строки:"))
        if stroka > 12 or stroka < 1:
            print('Не существующий номер!')
        else:
            break
    while True:
        stolb = int(input("Введите номер столбца:"))
        if stolb > 12 or stolb < 1:
            print('Не существующий номер!')
        else:
            break
    if myLib.pole[stroka-1][stolb-1] == '%':
        print('Игра окончена')
        break
    # передадим не номера строки и столбца, а индексы
    myLib.check(stroka-1,stolb-1)
    myLib.vyvodPolya(myLib.vidimost_polya)
    if myLib.isOpen():
        print('Все поле открыто!')
        game = False