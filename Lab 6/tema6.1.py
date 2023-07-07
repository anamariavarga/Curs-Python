# 1. Scrieti o functie care afiseaza toti elevii și mediile în felul urmator:

def media(p):
    if len(p) > 0:
        return round(sum(p) / len(p), 2)
    else:
        return 0.00


catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}
a = 50
b = 5
spacing = "-" * (a + b)

print(f"{'Elev' : <{a}}{'Media' : <{b}}")
print(spacing)
for k, v in catalog.items():
    print(f"{k: <{a}}{media(v) : >{b}.2f}")
