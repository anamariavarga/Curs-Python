def media(t: list) -> float:
    """Compute the average of values in the list"""

    if len(t) == 0:
        return 0
    return round(sum(t) / len(t), 2)


def media_best(t: list, how_many: int = 3) -> float:
    """Compute the average of best how_many values in the list"""

    t = sorted(t, reverse=True)[:how_many]
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


def create_final_catalog(c: dict, t: dict, file_name: str):
    """Create the final catalog"""

    n, m, d = 50, 2, 2

    with open(file_name, 'w', encoding='utf-8') as cat_final:
        header = f'{"Nume":{n}} {"Media":{m}}'
        print(header, file=cat_final)
        print('-' * len(header), file=cat_final)

        for el in sorted(c):
            media_total = media([media_best(c[el]), t[el]])
            print(f'{el:<{n}} {media_total:>{m}.{d}f}', file=cat_final)


def create_champions_catalog(c: dict, t: dict, file_name: str):
    """Create the champions catalog"""

    ch = {}
    for e, n in c.items():
        ch[e] = media([media_best(n), t[e]])

    champs = sorted(ch, key=ch.get, reverse=True)[:3]
    n, m, d, p = 50, 2, 2, 6

    with open(file_name, 'w', encoding='utf-8') as cat_final:
        header = f'{"Premiu":{p}} {"Nume":{n}} {"Media":{m}}'
        print(header, file=cat_final)
        print('-' * len(header), file=cat_final)

        for i, e in enumerate(champs, start=1):
            print(f'{i:^{p}} {e:<{n}} {ch[e]:>{m}.{d}f}', file=cat_final)


def create_unlucky_catalog(c: dict, t: dict, file_name: str):
    """Create the catalog of the unlucky ones"""

    unlucky = {}
    for e, n in c.items():
        unlucky[e] = media([media_best(n), t[e]])

    n, m, d, p = 50, 2, 2, 6

    with open(file_name, 'w', encoding='utf-8') as cat_final:
        header = f'{"Nume":{n}} {"Media":{m}}'
        print(header, file=cat_final)
        print('-' * len(header), file=cat_final)

        for e, me in unlucky.items():
            if me >= 5:
                continue
            print(f'{e:<{n}} {me:>{m}.{d}f}', file=cat_final)


catalog = get_catalog_from_file('../lab07/catalog.txt')
note_teze = get_teze_from_file('../lab07/teze.txt')

create_final_catalog(catalog, note_teze, '../lab07/medii_alfabetic.txt')
create_champions_catalog(catalog, note_teze, '../lab07/premiantii.txt')
create_unlucky_catalog(catalog, note_teze, '../lab07/corijenti.txt')








