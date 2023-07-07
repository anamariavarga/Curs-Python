# 5. Scrieti o functie de calcul a mediei, care are doi parametri elev și materia. Materia are ca valoare default None.
# - la apelul functiei, daca materia are vreuna dintre valorile m,r, sau f se va calcula media elevului la acea materie și se va
# afisa un mesaj sugestiv de genul: Elevul X are media la matematica 7.55
# - daca valoarea parametrului materia este None atunci se vor calcula mediile pentru fiecare materie și se va afisa mesajul:
# Elevul X are urmatoarele medii:
# matematica: 7.55
# limba romana: 6.78
# fizica: 5.60
def media(elev, materia):
    if elev not in catalog:
        print(f"Eroare! Elevul {elev} nu se afla in catalog.")
        return
    if materia not in materii:
        print('Eroare! Materie inexistenta')
        return
    note = catalog[elev][materia]
    if len(note) > 0:
        m = round(sum(note) / len(note))
    else:
        m = 0
    print('Media la materia', materii[materia], ' a elevului ', elev, ' este ', m)


catalog = {
    'Popescu Ion': {
        'm': [2, 5, 7],
        'f': [],
        'r': [6, 9, 8],
    },
    'Ionescu Geta': {
        'r': [6, 3, 8],
        'm': [4, 5],
        'f': [7, 9, 10]
    },
    'Georgescu Gelu': {
        'm': [2, 5, 7, 9],
        'r': [9, 8],
        'f': [6, 9]
    },
    'Radulescu Ioana': {
        'm': [7],
        'f': [],
        'r': [6, 9, 8],
    },
}

materii = {
    'm': 'matematica',
    'r': 'limba romana',
    'f': 'fizica',
}
media('Radulescu Ioana', 'r')
