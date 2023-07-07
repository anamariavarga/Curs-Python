import xlsxwriter


def media(t):
    """Compute the average of values in the list.

    Parameters
    ----------
    t : list
        the list of notes

    Returns
    ----------
    float:
        the average of the notes
    """

    if len(t) == 0:
        return 0
    return round(sum(t) / len(t), 2)


def get_catalog_from_file(file_name):
    """Reads the catalog from a text file

    Parameters
    ----------
    file_name : str
        the name of the input file

    Returns
    --------
    dict:
        the dictionary containing the catalog data
    """

    ca = {}
    with open(file_name, 'r', encoding='utf-8') as catalog_file:
        for line in catalog_file:
            el = line.strip().split(';')
            ca[el[0]] = list(map(int, el[1:]))
    return ca


def create_final_catalog(c, file_name):
    """Create the final catalog

    Parameters
    ----------
    c : dict
        the dictionary catalog
    file_name :
        the name of the output file
    """

    n, m, d = 25, 5, 2

    with open(file_name, 'w', encoding='utf-8') as cat_final:
        print(f'{"Nume":{n}} {"Prenume":{n}} {"Media":{m}} {"Note":>{m}}', file=cat_final)
        print('-' * (n + n + m + m + 3), file=cat_final)

        for elev, note in c.items():
            nume, prenume = elev.split()
            print(f'{nume:<{n}} {prenume:<{n}} {media(note):>{m}.{d}f} {len(note):^{m}}', file=cat_final)


def get_teze_from_file(file_name):
    """Reads 'teze' from a file

    Parameters
    ----------
    file_name : str
        the name of the input file
    """

    te = {}
    with open(file_name, 'r', encoding='utf-8') as teze:
        for line in teze:
            el = line.strip().split(';')
            te[el[0]] = int(el[1])
    return te


def create_catalog_xlsx(c, file_name):
    """Creates the catalog as xlsx file

    Parameters
    ----------
    c : dict
        the input catalog
    file_name : str
        the output file
    """

    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 40)
    worksheet.set_column('B:B', 10)
    bold = workbook.add_format({'bold': True})
    number_format = workbook.add_format({'num_format': '#0.00', 'align': 'right'})
    string_format = workbook.add_format({'align': 'left'})
    worksheet.write('A1', 'Elev', bold)
    worksheet.write('B1', 'Media', bold)

    for i, e in enumerate(sorted(c), start=2):
        worksheet.write(f'A{i}', e, string_format)
        worksheet.write(f'B{i}', media(c[e]), number_format)

    workbook.close()


if __name__ == '__main__':
    pass
