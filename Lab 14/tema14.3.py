from foca_geometry import *
p1 = Point(-13, 2)
p2 = Point(-5, 7)
p3 = Point(4, 3)
p4 = Point(4, -6)
p5 = Point(8, -4)
polyline = Polyline(p1, p2, p3, p4, p5)
print(polyline)

print('.........................................')
p = Polyline(Point(3, 7), Point(6, -12), Point(0.6, 0), Point(1, 1), )
print(p)