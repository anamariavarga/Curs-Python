from modules.geometry import Point, Rectangle

x1 = float(input('Introdu coordonata x a lui p1:'))
y1 = float(input('Introdu coordonata y a lui p1:'))
x2 = float(input('Introdu coordonata x a lui p2:'))
y2 = float(input('Introdu coordonata y a lui p2:'))

r = Rectangle(Point(x1, y1), Point(x2, y2))

print('Dimensiunile sunt: ', r.get_dimensions())
print('Aria este: ', r.get_area())
print('Perimetrul este', r.get_perimeter())
