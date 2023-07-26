from lab12.modules.geometry import Point

m1 = float(input('Introdu valoarea lui m1:'))
n1 = float(input('Introdu valoarea lui n1:'))

m2 = float(input('Introdu valoarea lui m2:'))
n2 = float(input('Introdu valoarea lui n2:'))

p1 = Point(m1, n1)
p2 = Point(m2, n2)

if p1.get_distance() < p2.get_distance():
    print('p2 este mai departe de centru decat p1')
elif p1.get_distance() > p2.get_distance():
    print('p1 este mai departe de centru decat p2')
else:
    print('p1 și p2 sunt la aceeasi distanta fata de centru')
