def media(t):
    if len(t) == 0:
        return 0
    return round(sum(t) / len(t), 2)


note = {
    'Popescu Ion': (2, 5, 7),
    'Ionescu Geta': (10, 7, 9, 7),
    'Georgescu Gelu': (4, 2),
    'Radulescu Ioana': (5, 9, 6, 4, 10)
}

lista_medii = []

for elev, note in list(note.items()):
    lista_medii.append((media(note), elev))

for media, elev in sorted(lista_medii, reverse=True):
    print(elev, media)

