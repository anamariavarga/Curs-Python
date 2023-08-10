import math


class WrongGeometry(Exception):
    pass


def absolute_value(a):
    if float(a) >= 0:
        return float(a)
    else:
        return float(-a)


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point ({self.x}, {self.y})'

    def get_distance(self):
        """
        This method calculate the distance from the origin of axis system to a specific point.

        Returns:
            float: The distance (rounded to two decimals)
        """
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)


class Circle(Point):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def get_area(self):
        """
        This method calculate the area of a circle.

        Returns:
            float: The area of the circle (rounded to two decimals)
        """
        return round(math.pi * self.r ** 2, 2)

    def get_distance(self):
        """
        This method calculate the distance from the origin of axis system to the circle's center.

        Returns:
            float: The distance (rounded to two decimals)
        """
        return super().get_distance() - self.r


class Rectangle:
    """
    Class for rectangle.

    Attributes:
       p1 (tuple): Coordinates for point p1(x, y).
       p2 (tuple): Coordinates for point p2(x, y).
    """
    instances = 0
    square_instances = 0

    def __init__(self, p1: Point, p2: Point):
        """
        Rectangle defined by two points: p1 and p2.

        Args:
          p1 (Point): Coordinates for point p1(x, y).
          p2 (Point): Coordinates for point p2(x, y).
        """
        self.p1 = p1
        self.p2 = p2
        self.length = abs(self.p1.x - self.p2.x)
        self.width = abs(self.p1.y - self.p2.y)
        Rectangle.instances += 1
        if self.rectangle_square():
            Rectangle.square_instances += 1

    @staticmethod
    def get_square_percent():
        square_rectangles = (Rectangle.square_instances / Rectangle.instances) * 100
        print(f'From the total numbers of rectangles, there are {round(square_rectangles, 2)} % square created '
              f'rectangles.')

    def __eq__(self, other):
        # if self.get_rectangle_dimensions() == other.get_rectangle_dimensions():
        #     return True
        # else:
        #     return False
        # return sorted([self.width, self.length]) == sorted([self.width, self.length])
        return sorted(self.get_rectangle_dimensions()) == sorted(other.get_rectangle_dimensions())

    def __str__(self):
        return f'Rectangle ( {self.p1}, {self.p2})'

    def get_rectangle_dimensions(self) -> list:
        """
        This method calculate and return the dimensions of a rectangle.
        The rectangle is defined by two points.

        Parameters:
            self (object): The instance of the class containing the two points.

        Returns:
            tuple: A tuple containing the calculated length and width of the rectangle.
        """
        # length = abs(self.p1.x - self.p2.x)
        # width = abs(self.p1.y - self.p2.y)
        return sorted([round(self.length, 2), round(self.width, 2)])

        # return [
        #     abs(self.p1.x - self.p2.x),
        #     abs(self.p1.y - self.p2.y),
        # ]

    def get_rectangle_area(self):
        """
         This method calculate the area of a rectangle.

         Returns:
             float: The area of the rectangle (rounded to two decimals)
         """
        length, width = self.get_rectangle_dimensions()
        return round(length * width, 2)

    def get_rectangle_perimeter(self):
        """
       This method calculate the perimeter of a rectangle.

       Returns:
           float: The perimeter of the rectangle (rounded to two decimals).
        """
        length, width = self.get_rectangle_dimensions()
        return round(2 * (length + width), 2)

    def point_in_or_out_rectangle(self, q: Point):
        """
        This method determines whether a given point q is inside or outside of a rectangle.
        The rectangle is defined by self.p1 and self.p2.

        Parameters:
            q (Point): The point to be checked.

        Returns:
            None: This method does not return any value. It prints the result directly.
        """
        # o varianta:
        # if (self.p1.x <= q.x <= self.p2.x or self.p2.x <= q.x <= self.p1.x) and \
        #         (self.p1.y <= q.y <= self.p2.y or self.p2.y <= q.y <= self.p1.y):
        #     print(f'The point {q.x, q.y} is inside the rectangle')
        # else:
        #     print(f'The point {q.x, q.y} is outside the rectangle')
        # alta varianta mai simpla:
        lx = sorted([self.p1.x, self.p2.x])
        ly = sorted([self.p1.y, self.p2.y])
        return lx[0] <= q.x <= lx[1] and ly[0] <= q.y <= ly[1]

    def circle_in_or_out_rectangle(self, q, r):
        """
        This method determines whether a circle is inside or outside of a rectangle.
        The rectangle is defined by self.p1 and self.p2.
        The circle is defined by a point and a radius.

        Parameters:
            q (Point): the point that indicates the center of the circle

        Returns:
            None: This method does not return any value. It prints the result directly.
        """
        # o varianta:
        if (self.p1.x <= (q.x + r) <= self.p2.x or self.p2.x <= (q.x + r) <= self.p1.x) and \
                (self.p1.y <= (q.y + r) <= self.p2.y or self.p2.y <= (q.y + r) <= self.p1.y):
            print(f'The circle with origin in {q.x, q.y} and radius {r} is inside the rectangle')
            # return True
        else:
            print(f'The circle with origin in {q.x, q.y} and radius {r} is outside the rectangle')
            # return False

    def rectangle_square(self):
        if self.length == self.width:
            return True
        else:
            return False
    #     # alta varianta mai simpla:
    # def circle_in_or_out_rectangle(self, c:Circle):
    #     lx = sorted([self.p1.x, self.p2.x])
    #     ly = sorted([self.p1.y, self.p2.y])
    #     return lx[0] <= c.x - c.r and c.x + c.r <= lx[1] \
    #         and ly[0] <= c.y - c.r and c.y + c.r <= ly[1]


class Polyline:
    def __init__(self, *points):
        for p in points:
            if type(p) != Point:
                raise WrongGeometry('Variabila trebuie sa fie de tip Point(x,y)!')
        self.points = points
        # self.p = args
        # for p in args:
        #     # if not isinstance(p, Point): # not ok
        #     if type(p) != Point:
        #         raise WrongGeometry('Only points allowed in constructor')
        # self.points = list(args)

    def __str__(self):
        p_list = ', '.join(map(lambda p: 'Point ' + str(p), self.p))
        return f'Polyline({p_list})'


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


if __name__ == '__main__':
    p2 = (-5, 7)
    p3 = (4, 3)
    p4 = (4, -6)
    p5 = (8, -4)
    polyline = Polyline(p1, p2, p3, p4, p5)
    print(polyline)
