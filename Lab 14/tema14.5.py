from foca_geometry import *

r1 = Rectangle(Point(5, 6), Point(6, 7))
r2 = Rectangle(Point(2, -19), Point(-20, 7))
r3 = Rectangle(Point(10, 6), Point(1, -31))
total_rectangles = Rectangle.instances
total_square_rectangles = Rectangle.square_instances

print(Rectangle.get_square_percent())
