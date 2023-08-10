from modules.geometry import Point, Rectangle

r1 = Rectangle(Point(6, 4), Point(2, 0))
r2 = Rectangle(Point(-34, 1), Point(-56.89, 9))

print(r1.is_square())
print(r2.is_square())
