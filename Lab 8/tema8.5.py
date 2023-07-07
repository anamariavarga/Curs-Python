import tema8_1_2.modules.utils as ut

catalog = ut.get_catalog_from_file('tema8_1_2/data/catalog.txt')
ut.create_catalog_xlsx(catalog, 'catalog.xlsx')
