from lab12.modules.geometry import Point, Circle


def display_dist(p):
    for e in p:
        print(e.get_distance())


def get_dist(e):
    return e.get_distance()


p1 = Point(4, 8.5)
p2 = Point(3, 4)
p3 = Point(-5, 6)
c = Circle(-100, 100, 2)
l = [c, p1, p2, p3]
display_dist(l)


l1 = sorted(l)

print('#################')

l1 = sorted(l, key=get_dist)
display_dist(l1)

print('#################')

l2 = sorted(l, key=Point.get_distance)
display_dist(l2)

print('#################')

l3 = sorted(l, key=lambda p: p.get_distance())
display_dist(l3)
