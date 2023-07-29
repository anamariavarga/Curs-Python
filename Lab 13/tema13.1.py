from foca_geometry import *

p1_x = float(input("x for p1 in cm: "))
p1_y = float(input("y for p1 in cm: "))
p2_x = float(input("x for p2 in cm: : "))
p2_y = float(input("y for p2 in cm: "))
p1 = Point(p1_x, p1_y)
p2 = Point(p2_x, p2_y)
rectangle = Rectangle(p1, p2)
# area = Rectangle(p1, p2)
# perimeter = Rectangle(p1, p2)
print('The rectangle length and width in cm are: ', rectangle.get_rectangle_dimensions())
print('The rectangle area is: ', rectangle.get_rectangle_area(), " cm")
print('The rectangle perimeter is: ', rectangle.get_rectangle_perimeter(), ' cm')
