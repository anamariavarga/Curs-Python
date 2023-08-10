from modules.geometry import Circle, Point, Polyline

p1 = Polyline(Point(3, 7), Point(6, -12), Point(0.6, 0), Point(1, 1))
print(p1)

# error
p2 = Polyline(Point(3, 7), Point(6, -12), Point(0.6, 0), Point(1, 1), Circle(0, 0, 7))
print(2)

