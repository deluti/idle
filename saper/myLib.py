import random
# массив поля, * — пустое поле, # — стена
pole = [["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","#","#","#","#","#"],
        ["*","*","*","#","#","#","#","#","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["#","#","#","#","*","*","*","*","*","#","#","#"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"]]

# то, что будет выводиться на экран
vidimost_polya=[["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"]]
def vyvodPolya(spisok):
    for stroka in spisok:
        for kletka in stroka:
            print(kletka,end='')
        print()
def check(stroka,stolb):
   # если клетка ещё не открыта
    if vidimost_polya[stroka][stolb] == "•":
        # открываем
        vidimost_polya[stroka][stolb] = pole[stroka][stolb]
        # если оно оказалось пустым
        if pole[stroka][stolb] == "*":
            # проверяем все соседние, только если они существуют
            # а то выйдем за пределы поля, Python ругать будет
            if stroka-1 >= 0:
                check(stroka-1,stolb)
                if stolb-1 >= 0:
                    check(stroka-1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka-1,stolb+1)
                    
            if stroka+1 < len(pole):
                check(stroka+1,stolb)
                if stolb-1 >= 0:
                    check(stroka+1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka+1,stolb+1)
                    
            if stolb-1 >= 0:
                    check(stroka,stolb-1)
            if stolb+1 < len(pole[stroka]):
                check(stroka,stolb+1)
def isOpen():
    # считаем, что поле открыто всё
    opened = True
    #для каждой строки в видимости поля
    for stroka in vidimost_polya:
        # если хотя бы в одной нашлось закрытое поле
        if "•" in stroka:
            # значит неправда, поле ещё не всё открыто
            opened = False
    return opened
def mins():
    global pole
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0    
    x = random.randint(1, 12)
    y = random.randint(1, 12)
    while True:
        x1 = random.randint(1, 12)
        if x1 == x:
            x1 = random.randint(1, 12)
        else:
            break
    while True:
        y1 = random.randint(1, 12)
        if y1 ==y:
            y1 = random.randint(1, 12)
        else:
            break
    
    while True:
        x2 = random.randint(1, 12)
        if x2 == x or x2 == x1:
            x2 = random.randint(1, 12)
        else:
            break
    while True:
        y2 = random.randint(1, 12)
        if y2 == y1 or y2 == y:
            y2 = random.randint(1, 12)
        else:
            break
    pole[x-1][y-1] = '%'
    pole[x1-1][y1-1] = '%'
    pole[x2-1][y2-1] = '%'
def prov():
    for x in pole:
        for y in pole:
            if pole[x][y] == '%' and pole[x-1][y] < 0:
                pole[x-1][y] = '1'
            if pole[x][y] == '%' and pole[x+1][y] < 0:
                pole[x+1][y] = '1'
            if pole[x][y] == '%' and pole[x][y-1] < 0:
                pole[x][y-1] = '1'
            if pole[x][y] == '%' and pole[x][y+1] < 0:
                pole[x][y-1] = '1'