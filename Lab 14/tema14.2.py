from foca_geometry import *
x1 = float(input("x for p1 in cm: "))
y1 = float(input("y for p1 in cm: "))
x2 = float(input("x for p2 in cm: : "))
y2 = float(input("y for p2 in cm: "))
p1 = Point(x1, y1)
p2 = Point(x2, y2)
rectangle = Rectangle(p1, p2)
print(rectangle.rectangle_square())

print('............................')
r1 = Rectangle(Point(6, 4), Point(2, 0))
r2 = Rectangle(Point(-34, 1), Point(-56.89, 9))

print(r1.rectangle_square())
print(r2.rectangle_square())