print("Exercitiul 3.3")

l = [9, 3.9, 20, -6.4, 0, 20.03]
print("a: cautati o functie care sa va returneze minimul și maximul dintr-o lista")

print("Min = ", min(l), "si max = ", max(l))
print("...................................................")

print("""b: incercati sa creati voi programul care parcurge lista și
 determina elementul cel mai mic respectiv cel mai mare""")

print("varianta 1")
m=l[0]
for e in l:
    if e>m:
        m=e
print("Maximult este: ", m)
print("...................................................")
print("varianta 2")
x, y = (sorted(l)[::len(l) - 1])
print("Min = ", x, "si max = ", y)
print("...................................................")
print("varianta 3")

l1 = sorted(l)
print("Min = ", l1[0], "si max = ", l1[len(l1) - 1])
print("...................................................")
print("varianta 4")
l = [9, 3.9, 20, -6.4, 0, 20.03]
max_el = float("-inf")
for i in range(0, len(l)):
    if max_el < l[i]:
        max_el = l[i]
min_el = float("-inf")
for i in range(0, len(l)):
    if min_el < l[i]:
        min_el = l[i]
print("Min = ", min_el, "si max = ", max_el)

print("""c:Ce se intampla la punctele a și b de mai sus daca lista contine și 
altceva decat numere? De exemplu stringuri pe langa numere. Mai merge? De ce?""")

# print("")
# l2 = [9, 3.9, 0, -6.4, "40", 8]
# z1, z2 = (sorted(l2)[::len(l2) - 1])
# #print("Min = ", z1, "si max = ", z2)
