import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)


class Circle(Point):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def get_area(self):
        return round(math.pi * self.r ** 2, 2)

    def get_distance(self):
        return super().get_distance() - self.r


if __name__ == '__main__':
    m = float(input('Introdu valoarea lui m:'))
    n = float(input('Introdu valoarea lui n:'))

    p = Point(m, n)
    print('Distanta de la punct la origine este:', p.get_distance())

