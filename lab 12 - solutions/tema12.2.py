from lab12.modules.geometry import Point

m = float(input('Introdu valoarea lui m:'))
n = float(input('Introdu valoarea lui n:'))

p = Point(m, n)
print('Distanta de la punct la origine este:', p.get_distance())

