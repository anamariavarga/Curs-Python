from geometry import Point

valoarea_pe_x = float(input("Introduceți valoarea coordonatei x: "))
valoarea_pe_y = float(input("Introduceți valoarea coordonatei y: "))

po1 = Point(valoarea_pe_x, valoarea_pe_y)
print("Distanța de la punct la origine este:", po1.get_distance())
