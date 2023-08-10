from foca_geometry import *
# Rectangle(Point(x1, y1), Point(x2, y2))
x1 = float(input("x for p1 in cm: "))
y1 = float(input("y for p1 in cm: "))
x2 = float(input("x for p2 in cm: : "))
y2 = float(input("y for p2 in cm: "))
p1 = Point(x1, y1)
p2 = Point(x2, y2)
rectangle = Rectangle(p1, p2)
print(rectangle)

print('................................')
r = Rectangle(Point(2, 3), Point(6, 9))

print(r)