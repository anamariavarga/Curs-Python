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


def get_teze_from_file(file_name: str) -> dict:
    """Reads 'teze' from a file"""

    te = {}
    with open(file_name, 'r', encoding='utf-8') as teze:
        for line in teze:
            el = line.strip().split(';')
            te[el[0]] = int(el[1])
    return te


def create_final_catalog(c: dict, file_name: str):
    """Create the final catalog"""

    n, m, d = 50, 2, 2

    with open(file_name, 'w', encoding='utf-8') as cat_final:
        header = f'{"Nume":{n}} {"Media":{m}}'
        print(header, file=cat_final)
        print('-' * len(header), file=cat_final)

        for el in sorted(c):
            print(f'{el:<{n}} {media(c[el]):>{m}.{d}f}', file=cat_final)


catalog = get_catalog_from_file('catalog.txt')
note_teze = get_teze_from_file('teze.txt')
create_final_catalog(catalog, 'catalog_final.txt')








