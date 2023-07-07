print('''Exercitiul 2.3 - Avem o lista goala. Se tasteaza un sir de caractere si
cand se tasteaza X atunci programul se intrerupe. 
Sirurile de caractere se adauga la inceputul listei: ''')
l = []
while True:
    s= input("Tasteaza un sir de caractere:")
    if s == "X":
        break
    l.insert(0,s)
print("Lista rezultata este: ", l)
print("..................................................................")
print("Sirurile de caractere se adauga la sfarsitul listei: ")
l = []
while True:
    s= input("Tasteaza un sir de caractere:")
    if s == "X":
        break
    l.append(s)
print("Lista rezultata este: ", l)
print("..................................................................")
print("De la Ciprian")
my_list = []

while True:
    s = input('Introdu sirul:')
    if s == 'X' or s == 'x':
        break
    else:
        my_list.append(s)

print(my_list)
