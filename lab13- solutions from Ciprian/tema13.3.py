from modules.geometry import Point, Rectangle

r = Rectangle(Point(-8, 10), Point(4, 6))

print(r.contains_point(Point(-5, 7)))
print(r.contains_point(Point(-50, 70)))
