def media(t: list) -> float:
    """Compute the average of values in the list"""

    if len(t) == 0:
        return 0
    return round(sum(t) / len(t), 2)


def get_catalog_from_file(file_name: str) -> dict:
    """Reads the catalog from a text file"""

    ca = {}
    with open(file_name, 'r', encoding='utf-8') as catalog_file:
        for line in catalog_file:
            el = line.strip().split(';')
            ca[el[0]] = list(map(int, el[1:]))
    return ca


def create_final_catalog(c: dict, file_name: str):
    """Create the final catalog"""
    n, m, d = 25, 5, 2

    with open(file_name, 'w', encoding='utf-8') as cat_final:
        print(f'{"Nume":{n}} {"Prenume":{n}} {"Media":{m}} {"Note":>{m}}', file=cat_final)
        print('-' * (n + n + m + m + 3), file=cat_final)

        for elev, note in c.items():
            nume, prenume = elev.split()
            print(f'{nume:<{n}} {prenume:<{n}} {media(note):>{m}.{d}f} {len(note):^{m}}', file=cat_final)


def get_teze_from_file(file_name: str) -> dict:
    """Reads 'teze' from a file"""

    te = {}
    with open(file_name, 'r', encoding='utf-8') as teze:
        for line in teze:
            el = line.strip().split(';')
            te[el[0]] = int(el[1])
    return te
