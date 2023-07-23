from geometry import Point

p1_x_value = float(input("Introduceți valoarea coordonatei x pentru p1: "))
p1_y_value = float(input("Introduceți valoarea coordonatei y pentru p1: "))
p2_x_value = float(input("Introduceți valoarea coordonatei x petru p2: "))
p2_y_value = float(input("Introduceți valoarea coordonatei y pentru p2: "))

p1 = Point(p1_x_value, p1_y_value)
p2 = Point(p2_x_value, p2_y_value)
print("Distanța de la punct la origine pentru p1 este:", p1.get_distance())
print("Distanța de la punct la origine pentru p2 este:", p2.get_distance())

if p1 > p2:
    print("p1 este mai departe de centru decat p2")

elif p2 > p1:
    print("p2 este mai departe de centru decat p1")
else:
    print("p1 si p2 sunt la acceasi distanta fata de centru")