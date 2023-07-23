from geometry import Point

#
# p1_x_value = float(input("Introduceți valoarea coordonatei x pentru p1: "))
# p1_y_value = float(input("Introduceți valoarea coordonatei y pentru p1: "))
# p2_x_value = float(input("Introduceți valoarea coordonatei x petru p2: "))
# p2_y_value = float(input("Introduceți valoarea coordonatei y pentru p2: "))
# p3_x_value = float(input("Introduceți valoarea coordonatei x petru p3: "))
# p3_y_value = float(input("Introduceți valoarea coordonatei y pentru p3: "))
#
# p1 = Point(p1_x_value, p1_y_value)
# p2 = Point(p2_x_value, p2_y_value)
# p3 = Point(p3_x_value, p3_y_value)
p1 = Point(4, 8.5)
p2 = Point(3, 4)
p3 = Point(-5, 6)
print("Distanța de la punct la origine pentru p1 este:", p1.get_distance())
print("Distanța de la punct la origine pentru p2 este:", p2.get_distance())
print("Distanța de la punct la origine pentru p3 este:", p3.get_distance())
l = [p1.get_distance(), p2.get_distance(), p3.get_distance()]
# l.append(p1.get_distance())
# l.append(p2.get_distance())
# l.append(p3.get_distance())
l_sorted = sorted(l)
print('Lista de puncte este:', l)
print(sorted(l))
print(sorted(l, key=float))
print(sorted(l, key=lambda a: float(a)))
#ltest = [5, -9, 0]

def check_list_is_sorted(li):
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            return False
    return True


if check_list_is_sorted(l_sorted):
    print(f"The list {l_sorted} is ascending.")
else:
    print(f"The list {l_sorted} is not ascending.")
