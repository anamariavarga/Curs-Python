import re

print("Exercitiul 3.4")

s = 'In livada noastra avem ciresi, meri, peri si pruni. Care fructe credeti ca se coc primele? Variante: perele, merele, prunele si apoi ciresele. Foarte gresit! Corect este: ciresele, merele, perele si apoi prunele.'

print("a: Cate propozitii sunt in textul de mai sus")

l1 = s.replace('.', '$').replace('!', '$').replace('?', '$')
print(l1.split('$'))
print("Numarul de propozitii din text este: ", len(l1.split('$')) - 1)


print(".......................................................................")


print("Numarul de propozitii din text este: ", len(re.split(r'[.!?]', s)) - 1)
print(".......................................................................")
print("Numarul de propozitii din text este: ",s.count(".")+s.count("?")+s.count("!"))



print("b. Cate cuvinte sunt in textul de mai sus")

print("Numarul de cuvinte din text este: ", len(s.split()))

print("c. Creati si afisati o lista cu toate cuvintele din textul de mai sus, litere mici si fara caractere speciale")

print("Lista este: ",(s.replace(',', '').replace('?', '').replace('!', '').replace(':', '').replace('.', '')).lower().split())
print(".......................................................................")
new_string = re.sub('[,?!:.]',"",s)
new2 = new_string.strip().lower().split()
print(new2)
print(".......................................................................")
l = []
for e in s.split():
    l.append(e.lower().strip('.:?!'))
print(l)
