# 1. Scrieți o funcție care adauga o nota la un elev. Functia are doi parametri: elev și nota. Functia ii adauga la
# lista de note a elevului nota data ca parametru. Functia trebuie sa verifice urmatoarele: - nota data ca parametru
# sa fie intre 0 și 10, altfel sa dea mesaj de eroare și sa nu adauge nota - elevul dat ca parametru sa existe în
# catalog, altfel sa dea mesaj de eroare
catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}


def adaugare_nota(elev, nota_noua):
    if nota_noua <= 0 or nota_noua > 10:
        print("Nota noua nu este o valoare cuprinsa intre 0 si 10")
        return

    if elev not in catalog:
        print("Elevul nu există în catalog.")
        return

    catalog[elev].append(nota_noua)


elev = input("Nume elev: ")
nota_noua = int(input("Nota de adaugat: "))
adaugare_nota(elev, nota_noua)
print(catalog)
print('.......................................................................')
catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}


def adaugare_nota(elev, nota_noua):
    if nota_noua <= 0 or nota_noua > 10:
        print("Nota noua nu este o valoare cuprinsa intre 0 si 10")
        return

    if elev not in catalog:
        print("Elevul nu există în catalog.")
        return

    catalog[elev].append(nota_noua)
adaugare_nota('Popescu Ion',8)
print(catalog)
adaugare_nota('Popescu Ionn',8)
adaugare_nota('Popescu Ionn',12)