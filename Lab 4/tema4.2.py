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
print('''Exercitiul 2. Scrieți un program care afișează unul sub altul numele complet al fiecărui elev alături de media notelor sale. Nu conteaza
ordinea afișării elevilor. Output-ul sa fie cat mai frumos, atat la punctul acesta cât și la următoarele. Las la latitudinea voastra sa
afisati rezultatele cat mai frumos și util. De data aceasta elevii sa fie afisati in ordine alfabetica''')
for k, v in d.items():
    print(k, round(mean(v), 2))
print(".....................................")
for k, v in sorted(d.items()):
    Media = (round(sum(v) / len(v), 2))
    print(k.center(30),Media)
Nume_elevi = list(d.keys())
Note = list(d.values())
Note_obtinute = [str(t) for t in Note]
print(f"{'Nume elevi' : <20}{'Note obtinute': ^20}{'Media obtinuta' : >10}")
for i in range(0, len(d)):
    print(f"{Nume_elevi[i] : <20}{Note_obtinute[i] : ^20}{Nume_elevi[i] : >10}")
