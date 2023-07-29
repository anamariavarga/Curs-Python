from foca_geometry import *

p1_x = float(input("x for p1 in cm: "))
p1_y = float(input("y for p1 in cm: "))
p2_x = float(input("x for p2 in cm: : "))
p2_y = float(input("y for p2 in cm: "))
p3_x = float(input("x for p3 in cm: "))
p3_y = float(input("y for p3 in cm: "))
p4_x = float(input("x for p4 in cm: : "))
p4_y = float(input("y for p4 in cm: "))

p1 = Point(p1_x, p1_y)
p2 = Point(p2_x, p2_y)
p3 = Point(p3_x, p3_y)
p4 = Point(p4_x, p4_y)

rectangle1 = Rectangle(p1, p2)
rectangle2 = Rectangle(p3, p4)
print(f'The {rectangle1} length and width are: ', rectangle1.get_rectangle_dimensions())
print(f'The {rectangle2} length and width are: ', rectangle2.get_rectangle_dimensions())

print("Both rectangles have the same dimensions? -> "
      , rectangle1.get_rectangle_dimensions() == rectangle2.get_rectangle_dimensions())
