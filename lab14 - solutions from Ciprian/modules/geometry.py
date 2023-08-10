import math


class WrongGeometry(Exception):
    pass


class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def get_distance(self) -> float:
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)


class Circle(Point):

    def __init__(self, x: float, y: float, r: float):
        super().__init__(x, y)
        self.r = r

    def __str__(self):
        return f'Circle({self.x}, {self.y}, {self.r})'

    def get_area(self) -> float:
        return round(math.pi * self.r ** 2, 2)

    def get_distance(self) -> float:
        return super().get_distance() - self.r


class Segment:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # Segment(Point(3, 4), Point(5, 6))
        # return f'Segment(Point({self.p1.x}, {self.p1.y}), Point({self.p2.x}, {self.p2.y}))'
        return f'Segment({self.p1}, {self.p2})'

    def __lt__(self, other):
        return self.get_length() < other.get_length()

    def __le__(self, other):
        return self.get_length() <= other.get_length()

    def __gt__(self, other):
        return self.get_length() > other.get_length()

    def __ge__(self, other):
        return self.get_length() >= other.get_length()

    def get_length(self):
        return round(((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2) ** 0.5, 2)


class Rectangle:

    instances = 0
    square_instances = 0

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        Rectangle.instances += 1
        if self.is_square():
            Rectangle.square_instances += 1

    def __eq__(self, other):
        return sorted(self.get_dimensions()) == sorted(other.get_dimensions())

    def __str__(self):
        return f'Rectangle({self.p1}, {self.p2})'

    def get_dimensions(self) -> list:
        return [
            abs(self.p1.x - self.p2.x),
            abs(self.p1.y - self.p2.y),
        ]

    def get_area(self) -> float:
        d = self.get_dimensions()
        return d[0] * d[1]

    def get_perimeter(self) -> float:
        d = self.get_dimensions()
        return 2 * (d[0] + d[1])

    def contains_point(self, p: Point) -> bool:
        return (
                (self.p1.x <= p.x <= self.p2.x) or (self.p2.x <= p.x <= self.p1.x)
                and
                (self.p1.y <= p.y <= self.p2.y) or (self.p2.y <= p.y <= self.p1.y)
        )

    def contains_circle(self, c: Circle) -> bool:
        r_x = sorted([self.p1.x, self.p2.x])
        c_x = [c.x - c.r, c.x + c.r]
        r_y = sorted([self.p1.y, self.p2.y])
        c_y = [c.y - c.r, c.y + c.r]

        return (
                (r_x[0] <= c_x[0] and c_x[1] <= r_x[1])
                and
                (r_y[0] <= c_y[0] and c_y[1] <= r_y[1])
        )

    def is_square(self) -> bool:
        d = self.get_dimensions()
        return d[0] == d[1]

    @staticmethod
    def squares_percent():
        return round(Rectangle.square_instances * 100 / Rectangle.instances, 2)


class Polyline:

    def __init__(self, *args: Point):
        for p in args:
            # if not isinstance(p, Point): # not ok
            if type(p) != Point:
                raise WrongGeometry('Only points allowed in constructor')
        self.points = list(args)

    def __str__(self):
        s = 'Polyline('
        for p in self.points:
            s += f'{p}, '
        s = s.rstrip(', ') + ')'
        return s


if __name__ == '__main__':
    pass

