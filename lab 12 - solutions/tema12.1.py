class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)


m = float(input('Introdu valoarea lui m:'))
n = float(input('Introdu valoarea lui n:'))

p = Point(m, n)
print('Distanta de la punct la origine este:', p.get_distance())
