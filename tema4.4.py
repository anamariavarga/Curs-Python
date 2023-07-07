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
print('''Exercitiul 4. Scrieți un program care pe baza dicționarului de mai sus, creeaza un alt dictionar cu corigentii, adică cei cu media sub 5.
Dicționarul asta sa arate cam așa:
{ 'Georgescu Gelu': n,
…
}
Unde cheia este numele elevului iar n este media lui.
''')
corig = dict()
for k, v in d.items():
    if mean(v)<5:
        corig[k] = round(mean(v),2)
for k, v in corig.items():
    print(k,v)