#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

def getDistance(x1,y1,x2,y2):
    result = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return result
a = int(input("Введитe x1 \n"))
b = int(input("Введитe y1 \n"))
c = int(input("Введитe x2 \n"))
d = int(input("Введитe y1 \n"))
num = getDistance(a,b,c,d)
print(round(num,3))