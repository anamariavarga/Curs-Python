from geometry import Circle

valoarea_pe_x = float(input("Introduceți valoarea coordonatei x: "))
valoarea_pe_y = float(input("Introduceți valoarea coordonatei y: "))
raza_cercului = float(input("Introduceți valoarea razei cercului r: "))
a1 = Circle(valoarea_pe_x, valoarea_pe_y, raza_cercului)
print("Aria cercului este: ", a1.get_area())
print("Distanta de la origine la cerc este: ", a1.get_distance_from_center_to_circle())