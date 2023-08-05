from foca_geometry import *

p1_x = float(input("x for p1 in cm: "))
p1_y = float(input("y for p1 in cm: "))
p2_x = float(input("x for p2 in cm: : "))
p2_y = float(input("y for p2 in cm: "))
q_x = float(input("x for q in cm: "))
q_y = float(input("y for q in cm: "))
r = float(input("the circle radius is: "))

p1 = Point(p1_x, p1_y)
p2 = Point(p2_x, p2_y)
q = Point(q_x, q_y)

rectangle = Rectangle(p1, p2)
print('The rectangle length and width are: ', rectangle.get_rectangle_dimensions())
print('The rectangle area is: ', rectangle.get_rectangle_area())
print('The rectangle perimeter is: ', rectangle.get_rectangle_perimeter())
print("The point is inside the rectangle? ", rectangle.point_in_or_out_rectangle(q))
print(rectangle.circle_in_or_out_rectangle(q, r))