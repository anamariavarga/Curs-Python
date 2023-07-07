
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



catalog = get_catalog_from_file('catalog.txt')
n, m, d = 32, 5, 2
header = f'{"Nume":{n}} {"Media":{m}}'
print(header)
print('-' * len(header))

for elev in catalog:
    me = media(catalog[elev])
    print(f'{elev:<{n}} {me:>{m}.{d}f}')


