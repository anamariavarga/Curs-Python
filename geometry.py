# from math import sqrt
class Point:
    def __init__(self, x, y):
        self.distance = None
        self.x_coordinate = x
        self.y_coordinate = y

    def get_distance(self) -> str:
        self.distance = float((self.x_coordinate ** 2 + self.y_coordinate ** 2) ** 0.5)
        return f'{round(self.distance, 2)}'

    def __lt__(self, other):
        return self.get_distance() < other.get_distance()

    def __gt__(self, other):
        return self.get_distance() > other.get_distance()


class Circle(Point):
    def __init__(self, x, y, r) -> str:
        super().__init__(x, y)
        self.area = None
        self.distance_from_center_to_circle = None
        self.radius = r

    def get_area(self):
        self.area = 3.1416 * (float(self.radius) ** 2)
        return self.area

    def get_distance_from_center_to_circle(self):
        self.distance = float((self.x_coordinate ** 2 + self.y_coordinate ** 2) ** 0.5)
        self.distance_from_center_to_circle = self.distance - self.radius
        return f'{round(self.distance_from_center_to_circle, 2)}'


if __name__ == "__main__":
    valoarea_pe_x = float(input("Introduceți valoarea coordonatei x: "))
    valoarea_pe_y = float(input("Introduceți valoarea coordonatei y: "))
    raza_cercului = float(input("Introduceți valoarea razei cercului r: "))

    po1 = Point(valoarea_pe_x, valoarea_pe_y)
    a1 = Circle(valoarea_pe_x, valoarea_pe_y, raza_cercului)
    print("Distanța de la punct la origine este:", po1.get_distance())
    print("Aria cercului este: ", a1.get_area())
    print("Distanta de la origine la cerc este: ", a1.get_distance_from_center_to_circle())


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

