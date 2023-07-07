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
print(''' Exercitiul 1. Scrieți un program care afișează unul sub altul numele complet al fiecărui elev alături de media notelor sale. Nu conteaza
ordinea afișării elevilor. Output-ul sa fie cat mai frumos, atat la punctul acesta cât și la următoarele. Las la latitudinea voastra sa
afisati rezultatele cat mai frumos și util.''')

for k, v in d.items():
    print(k.center(30), round(sum(v) / len(v), 2))
print("................................................")
for k, v in d.items():
    print(k, round(mean(v), 2))
print("................................................")
for k, v in d.items():
    s = 0
    for e in v:
        s += e
    print(k, round(s/len(v), 2))
print("................................................")
