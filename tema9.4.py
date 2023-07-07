# 4. Creați un comprehension care sa genereze o listă conținând toate numerele din intervalul 0-100 care sunt
# divizibile cu 3 și nu sunt divizibile cu 5.
l = [x for x in range(0,101) if x % 3 == 0 and x % 5 != 0]
print(l)