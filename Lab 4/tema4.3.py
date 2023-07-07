# Avem următorul dicționar unde cheile sunt numele elevilor unei școli (sub forma nume de familie, spatiu, prenume) iar valorile
# cheilor sunt niște tuple cu notele elevilor:
from statistics import mean

d = {
    'Popescu Ion': (2, 5, 7),
    'Ionescu Geta': (10, 7, 9, 7),
    'Georgescu Gelu': (4, 2),
    'Radulescu Ioana': (5, 9, 6, 4, 10),
    'Ionescu Temistocle': (2, 9, 4, 10),
    'Popescu Electra': (2, 5, 3),
    'Bengescu Hortensia': (9,),
    'Popescu Sandokan': (7, 6, 7),
}
print('''Exercitiul 3. Scrieți un program care afișează unul sub altul numele complet al fiecărui elev alături de media notelor sale. Nu conteaza
ordinea afișării elevilor. Output-ul sa fie cat mai frumos, atat la punctul acesta cât și la următoarele. Las la latitudinea voastra sa
afisati rezultatele cat mai frumos și util. De data aceasta elevii sa fie afișați în ordine inversa a mediilor, adică cei cu media mai mare sus și mergând în jos spre
mediile mai mici''')
l=[]
for k, v in d.items():
    l.append((round(mean(v),2),k))
l.sort(reverse=True)
for m,e in l:
    print(e.center(30),m)