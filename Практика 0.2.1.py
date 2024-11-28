piece = input('Введите имя бравого воина с маленькой буквы: ')
print('Пусть обе оси (X и Y) будут отсчитываться натуральными числами от 1 до 8.')
print('Примем так-же тот факт, что пешки не могут находиться на 1-ой горизонтали')
print('Введите 4 координаты через enter, где первые две - начальные, вторые две - конечные.')
print('p.s.: сначала X потом Y.')
x_st, y_st = int(input()), int(input())
x_fin, y_fin = int(input()), int(input())
i = 1

if piece == 'слон':
    while i != 9:
        if x_fin == (x_st + i) and y_fin == (y_st + i):
            print('Может')
            break
        elif x_fin == (x_st - i) and y_fin == (y_st + i):
            print('Может')
            break
        elif x_fin == (x_st + i) and y_fin == (y_st - i):
            print('Может')
            break
        elif x_fin == (x_st - i) and y_fin == (y_st - i):
            print('Может')
            break
        else:
            if i < 9:
                i += 1
            else:
                print('Не может')
                break

elif piece == 'ладья':
    while i != 9:
        if x_fin == (x_st + i) and y_fin == y_st:
            print('Может')
            break
        elif x_fin == x_st and y_fin == (y_st + i):
            print('Может')
            break
        elif x_fin == x_st and y_fin == (y_st - i):
            print('Может')
            break
        elif x_fin == (x_st - i) and y_fin == y_st:
            print('Может')
            break
        else:
            if i < 9:
                i += 1
            else:
                print('Не может')
                break

elif piece == 'ферзь' or 'королева':
    while i != 9:
        if x_fin == (x_st + i) and y_fin == (y_st + i):
            print('Может')
            break
        elif x_fin == (x_st - i) and y_fin == (y_st + i):
            print('Может')
            break
        elif x_fin == (x_st + i) and y_fin == (y_st - i):
            print('Может')
            break
        elif x_fin == (x_st - i) and y_fin == (y_st - i):
            print('Может')
            break
        elif x_fin == (x_st + i) and y_fin == y_st:
            print('Может')
            break
        elif x_fin == x_st and y_fin == (y_st + i):
            print('Может')
            break
        elif x_fin == x_st and y_fin == (y_st - i):
            print('Может')
            break
        elif x_fin == (x_st - i) and y_fin == y_st:
            print('Может')
            break
        else:
            if i < 9:
                i += 1
            else:
                print('Не может')
                break

elif piece == 'конь':
    if x_fin == (x_st + 1) and y_fin == (y_st + 2):
        print('Может')
    elif x_fin == (x_st + 2) and y_fin == (y_st + 1):
        print('Может')
    if x_fin == (x_st - 1) and y_fin == (y_st + 2):
        print('Может')
    elif x_fin == (x_st - 2) and y_fin == (y_st + 1):
        print('Может')
    if x_fin == (x_st + 1) and y_fin == (y_st - 2):
        print('Может')
    elif x_fin == (x_st + 2) and y_fin == (y_st - 1):
        print('Может')
    if x_fin == (x_st + 1) and y_fin == (y_st + 2):
        print('Может')
    elif x_fin == (x_st - 2) and y_fin == (y_st - 1):
        print('Может')
    else:
        print('Не может')

elif piece == 'король':
    if x_fin == (x_st + 1) and y_fin == (x_st + 1):
        print('Может')
    elif x_fin == (x_st - 1) and y_fin == (x_st + 1):
        print('Может')
    elif x_fin == (x_st + 1) and y_fin == (x_st - 1):
        print('Может')
    elif x_fin == (x_st - 1) and y_fin == (x_st - 1):
        print('Может')
    elif x_fin == x_st and y_fin == (y_st + 1):
        print('Может')
    elif x_fin == x_st and y_fin == (y_st - 1):
        print('Может')
    elif x_fin == (x_st + 1) and y_fin == y_st:
        print('Может')
    elif x_fin == (x_st - 1) and y_fin == y_st:
        print('Может')
    else:
        print('Не может')

elif piece == 'пешка':
    if y_st == 2 and y_fin == (3 or 4) and x_fin == x_st:
        print('Может')
    elif y_fin == y_st + 1 and x_fin == x_st:
        print('Может')
    else:
        print('Не может')
