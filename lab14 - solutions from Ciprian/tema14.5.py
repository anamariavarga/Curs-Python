from modules.geometry import Point, Rectangle

r1 = Rectangle(Point(3, 3), Point(-2, -2))
r2 = Rectangle(Point(-3, 3), Point(-2, -2))
r3 = Rectangle(Point(3, 3), Point(-12, -2))
r4 = Rectangle(Point(3, 3), Point(-2, -2))

print(Rectangle.instances, Rectangle.square_instances, Rectangle.squares_percent())
