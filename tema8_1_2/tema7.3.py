from modules.utils import get_catalog_from_file, media

catalog = get_catalog_from_file('data/catalog.txt')
cat_sortat = sorted(catalog, key=catalog.get, reverse=True)[:3]
for p, elev in enumerate(cat_sortat, start=1):
    print(p, elev, media(catalog[elev]))
