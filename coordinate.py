#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

def quaterFromcordinate(x,y):
    result = 0
    if x > 0 and y > 0:
        result = 1
    elif x < 0 and y < 0:
        result = 3
    elif x > 0 and y < 0:
        result = 4
    elif x < 0 and y < 0:
        result = 2
    else:
        result = "Точка лежит на оси координат"
    return result
x = int(input("Введите x "))
y = int(input("Введите y "))
rez = quaterFromcordinate(x,y)
print(rez)