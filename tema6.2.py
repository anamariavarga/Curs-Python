#2. La fel ca la punctul anterior dar defalcam numele elevului pe nume și prenume


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
a = 25
b = 5
spacing = "-" * (a + a + b)
print(f"{'Nume' : <{a}}{'Prenume':<{a}}{'Media' : <{b}}")
print(spacing)
for k, v in catalog.items():
    print(f"{k.split()[0]: <{a}}{k.split()[1]: <{a}}{media(v) : >{b}.2f}")
print("*****************************************************************")
print(f"{'Nume' :<{a}}{'Prenume':<{a}}{'Media' :<{b}}")
print(spacing)
for k, v in catalog.items():
    nume, prenume = k.split()
    print(f"{nume: <{a}}{prenume: <{a}}{media(v) : >{b}.2f}")