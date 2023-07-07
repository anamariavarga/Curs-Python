# 2. Mai adaugati un parametru funcției de la punctul anterior numit overwrite, cu o valoare default False
# - daca overwrite este False functia va functiona exact cum e descris la punctul anterior
# - daca overwrite este True atunci nota data ca parametru va inlocui toate celelalte note existente. Practic elevul va avea în
# acest caz o singura nota în lista și anume nota data ca parametru
catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}
# def adaugare_nota(elev, nota_noua, overwrite = False):
#
#     if nota_noua <= 0 or nota_noua > 10:
#         print("Eroare: Nota noua nu este o valoare cuprinsa intre 0 si 10")
#         return
#
#     if elev not in catalog:
#         print("Eroare: Elevul nu există în catalog.")
#         return
#     if overwrite:
#         catalog[elev] = [nota_noua]
#     else:
#         catalog[elev].append(nota_noua)
#
# elev = input("Nume elev: ")
# nota_noua = int(input("Nota de adaugat: "))
# overwrite = input("Se inlocuiesc notele existente? ").lower()== "da"
# adaugare_nota(elev, nota_noua, overwrite)
# print(catalog)
print(".................................................................................")
def adaugare_nota(elev, nota_noua, overwrite = False):

    if nota_noua <= 0 or nota_noua > 10:
        print("Eroare: Nota noua nu este o valoare cuprinsa intre 0 si 10")
        return

    if elev not in catalog:
        print("Eroare: Elevul nu există în catalog.")
        return
    if overwrite:
        catalog[elev] = [nota_noua]
    else:
        catalog[elev].append(nota_noua)

print(catalog)
adaugare_nota("Ionescu Geta",1)
print(catalog)
adaugare_nota("Ionescu Geta",1, True)
print(catalog)
adaugare_nota("Ionescu Getasss",1, True)

