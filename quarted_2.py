#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
# точек в этой четверти (x и y).

def getCordinateFromQuater(number):
    result = 0
    if number == 1:
        result = "X > 0 , y > 0"
    elif number == 3:
        result = "X < 0 , y < 0"
    elif number == 4:
        result = "X > 0 , y < 0"
    elif number == 2:
        result = "X < 0 , y > 0"
    else:
        result = "такой четверти не существует"
    return result
a = int(input("Введите номер четверти \n"))
print(getCordinateFromQuater(a))