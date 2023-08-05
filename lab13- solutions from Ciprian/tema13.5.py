from modules.geometry import Point, Rectangle

r1 = Rectangle(Point(-5, 5), Point(1, 3))
r2 = Rectangle(Point(10, 8), Point(8, 2))
r3 = Rectangle(Point(100, 80), Point(200, 3))

if r1 == r2:
    print('Dreptunghiurile sunt egale')
else:
    print('Dreptunghiurile nu sunt egale')

if r1 == r3:
    print('Dreptunghiurile sunt egale')
else:
    print('Dreptunghiurile nu sunt egale')
