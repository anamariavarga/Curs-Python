from math import sqrt
class Point:
    def __init__(self, x, y):
        self.distance = None
        self.x_coordinate = x
        self.y_coordinate = y

    def get_distance(self) -> str:
        self.distance = float(sqrt(self.x_coordinate ** 2 + self.y_coordinate ** 2))
        return f'{round(self.distance,2)}'

if __name__ == "__main__":
    valoarea_pe_x = float(input("Introduceți valoarea coordonatei x: "))
    valoarea_pe_y = float(input("Introduceți valoarea coordonatei y: "))

    po1 = Point(valoarea_pe_x, valoarea_pe_y)
    print("Distanța de la punct la origine este:", po1.get_distance())



