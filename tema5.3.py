# 3. Scrieti o functie care sterge note, cu doi parametri elev și nota iar nota sa aiba o valoare default None.
# - daca nota are o valoare diferita de None se va cauta nota în lista de note a elevului și daca exista se va sterge. Daca are
# mai multe note de 7 de exemplu, se va sterge oricare, nu conteaza. Daca nu exista nota, se va afisa un mesaj de eroare
# sugestiv.
# - daca nota este None, vor disparea toate notele elevului și va avea o lista de note goala.
catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}


def stergere_nota(elev, nota_specificata=None):
    if elev not in catalog:
        print('Eroare! Elevul nu exista.')
        return
    if nota_specificata is None:
        catalog[elev] = []
    else:
        if nota_specificata in catalog[elev]:
            catalog[elev].remove(nota_specificata)
        else:
            print('Eroare! Elevul nu are nota respectiva.')

print(catalog)
stergere_nota('Georgescu Gelu',4)
print(catalog)
stergere_nota('Georgescu Gelu')
print(catalog)