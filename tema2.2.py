import math

print("Exercitiul 2.2")
print("")
print("Se introduc pe rând de la tastatura trei numere, a, b și c. Ele reprezinta lungimile laturilor unui triunghi.")
a = float(input("In cm latura a este: "))
print(a)
b = float(input("In cm latura b este: "))
print(b)
c = float(input("In cm latura c este: "))
print("Se cere sa se afiseze tipul triunghiului:")

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input. Laturile triunghiului nu pot avea valori negative sau egale cu 0.")
if a + b <= c or a + c <= b or b + c <= a:
    print("Laturile introduse nu formeaza un triunghi")
elif a == b and b == c and c == a:
    print("Triunghiul este echilateral")
elif math.sqrt(a ** 2 + b ** 2) == c or math.sqrt(a ** 2 + c ** 2) == b or math.sqrt(b ** 2 + c ** 2) == a:
    print("Triunghiul este dreptunghic")
elif a == b or a == c or b == c:
    print("Triunghiul este isoscel")
else:
    print("Triunghiul este oarecare")
print(".......................................................................................................")
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input. Laturile triunghiului nu pot avea valori negative sau egale cu 0.")
if a + b <= c or a + c <= b or b + c <= a:
    print("Laturile introduse nu formeaza un triunghi")
elif a == b == c:
    print("Triunghiul este echilateral")
elif a == b or b == c or c == a:
    print("Triunghiul este isoscel")
elif a * a == b * b + c * c or b * b == a * a + c * c or c * c == b * b + a * a:
    print("Triunghiul este dreptunghic")
else:
    print("Triunghiul este oarecare")
print(".......................................................................................................")
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input. Laturile triunghiului nu pot avea valori negative sau egale cu 0.")
if a + b <= c or a + c <= b or b + c <= a:
    print("Laturile introduse nu formeaza un triunghi")
elif a == b == c:
    print("Triunghiul este echilateral")
elif a == b or b == c or c == a:
    print("Triunghiul este isoscel")
elif a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2:
    print("Triunghiul este dreptunghic")
else:
    print("Triunghiul este oarecare")
print(".......................................................................................................")
print("De la Ciprian")
a = float(input('Introdu lungimea laturii a: '))
b = float(input('Introdu lungimea laturii b: '))
c = float(input('Introdu lungimea laturii c: '))

echilateral = (a == b == c)
isoscel = (a == b or b == c or c == a)
dreptunghic = (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) or (c ** 2 == a ** 2 + b ** 2)

if echilateral:
    print('Triunghiul este echilateral')
elif isoscel:
    print('Triunghiul este isoscel')
elif dreptunghic:
    print('Triunghiul este dreptunghic')
else:
    print('Triunghiul este oarecare')
print(".......................................................................................................")