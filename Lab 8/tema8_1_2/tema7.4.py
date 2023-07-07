import modules.utils as ut

catalog = ut.get_catalog_from_file('data/catalog.txt')
note_teze = ut.get_teze_from_file('data/teze.txt')
ut.create_final_catalog(catalog, 'data/catalog_final.txt')
