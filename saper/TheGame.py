import myLib
from myLib import prov
from myLib import pole
myLib.mins()
prov()
game = True
while game:
    run = 0
    run1 = False
    run2 = False
    while True:
        print('Что делаем?(1-флаг, 2-ход)')
        run = input()
        if run == '1':
            run1 = True
            break
        elif run == '2':
            run2 = True
            break
        else:
            print('неверные данные!')
    while(run1):
        stroka = int(input("Введите номер строки:"))
        if stroka > 12 or stroka < 1:
            print('Не существующий номер!')
        else:
            break
    while(run1):
        stolb = int(input("Введите номер столбца:"))
        if stolb > 12 or stolb < 1:
            print('Не существующий номер!')
        else:
            break
    #================================================
    while(run2):
        while(run2):
            stroka = int(input("Введите номер строки:"))
            if stroka > 12 or stroka < 1:
                print('Не существующий номер!')
            else:
                break
        while(run2):
            stolb = int(input("Введите номер столбца:"))
            if stolb > 12 or stolb < 1:
                print('Не существующий номер!')
            else:
                break
        pole[stroka][stolb] = '!'
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