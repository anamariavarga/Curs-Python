from modules.utils import *

catalog = get_catalog_from_file('data/catalog.txt')
n, m, d = 32, 5, 2
header = f'{"Nume":{n}} {"Media":{m}}'
print(header)
print('-' * len(header))

for elev in catalog:
    me = media(catalog[elev])
    print(f'{elev:<{n}} {me:>{m}.{d}f}')


