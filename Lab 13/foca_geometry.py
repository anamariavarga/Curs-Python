import math


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
        return f'({self.x}, {self.y})'

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

    def __init__(self, p1, p2):
        """
        Rectangle defined by two points: p1 and p2.

        Args:
          p1 (tuple): Coordinates for point p1(x, y).
          p2 (tuple): Coordinates for point p2(x, y).
        """
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'Rectangle from {self.p1} to {self.p2}'

    def get_rectangle_dimensions(self):
        """
        This method calculate and return the dimensions of a rectangle.
        The rectangle is defined by two points.

        Parameters:
            self (object): The instance of the class containing the two points.

        Returns:
            tuple: A tuple containing the calculated length and width of the rectangle.
        """
        length = self.p2.x - self.p1.x
        width = self.p1.y - self.p2.y
        return round(length, 2), round(width, 2)

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

    def point_in_or_out_rectangle(self, q):
        """
        This method determines whether a given point q is inside or outside of a rectangle.
        The rectangle is defined by self.p1 and self.p2.

        Parameters:
            q (Point): The point to be checked.

        Returns:
            None: This method does not return any value. It prints the result directly.
        """
        if (self.p1.x <= q.x <= self.p2.x or self.p2.x <= q.x <= self.p1.x) and \
                (self.p1.y <= q.y <= self.p2.y or self.p2.y <= q.y <= self.p1.y):
            print(f'The point {q.x, q.y} is inside the rectangle')
        else:
            print(f'The point {q.x, q.y} is outside the rectangle')

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
        if (self.p1.x <= (q.x + r) <= self.p2.x or self.p2.x <= (q.x + r) <= self.p1.x) and \
                (self.p1.y <= (q.y + r) <= self.p2.y or self.p2.y <= (q.y + r) <= self.p1.y):
            print(f'The circle with origin in {q.x, q.y} and radius {r} is inside the rectangle')
            # return True
        else:
            print(f'The circle with origin in {q.x, q.y} and radius {r} is outside the rectangle')
            # return False

    def __eq__(self, other):
        if self.get_rectangle_dimensions() == other.get_rectangle_dimensions():
            return True
        else:
            return False


if __name__ == '__main__':
    # p1_x = float(input("x for p1 in cm: "))
    # p1_y = float(input("y for p1 in cm: "))
    # p2_x = float(input("x for p2 in cm: : "))
    # p2_y = float(input("y for p2 in cm: "))
    # q_x = float(input("x for q in cm: "))
    # q_y = float(input("y for q in cm: "))
    # r = float(input("the circle radius is: "))
    #
    # p1 = Point(p1_x, p1_y)
    # p2 = Point(p2_x, p2_y)
    # q = Point(q_x, q_y)
    #
    # rectangle = Rectangle(p1, p2)
    # print('The rectangle length and width are: ', rectangle.get_rectangle_dimensions())
    # print('The rectangle area is: ', rectangle.get_rectangle_area())
    # print('The rectangle perimeter is: ', rectangle.get_rectangle_perimeter())
    # print(rectangle.point_in_or_out_rectangle(q))
    # print(rectangle.circle_in_or_out_rectangle(q, r))

    p1_x = float(input("x for p1 in cm: "))
    p1_y = float(input("y for p1 in cm: "))
    p2_x = float(input("x for p2 in cm: : "))
    p2_y = float(input("y for p2 in cm: "))
    p3_x = float(input("x for p3 in cm: "))
    p3_y = float(input("y for p3 in cm: "))
    p4_x = float(input("x for p4 in cm: : "))
    p4_y = float(input("y for p4 in cm: "))

    p1 = Point(p1_x, p1_y)
    p2 = Point(p2_x, p2_y)
    p3 = Point(p3_x, p3_y)
    p4 = Point(p4_x, p4_y)

    rectangle1 = Rectangle(p1, p2)
    rectangle2 = Rectangle(p3, p4)
    print(f'The {rectangle1} length and width are: ', rectangle1.get_rectangle_dimensions())
    print(f'The {rectangle2} length and width are: ', rectangle2.get_rectangle_dimensions())
