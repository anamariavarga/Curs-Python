from lab12.modules.geometry import Circle

x = float(input('Introdu valoarea lui x:'))
y = float(input('Introdu valoarea lui y:'))
r = float(input('Introdu valoarea lui r:'))

c = Circle(x, y, r)

print('Distanta de la cerc la origine este:', c.get_distance())
print('Aria cercului este:', c.get_area())

