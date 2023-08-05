from modules.geometry import Circle, Point, Rectangle

r = Rectangle(Point(-8, 10), Point(4, 6))

print(r.contains_circle(Circle(-2, 8, 0.5)))
print(r.contains_circle(Circle(-2, 8, 5)))
