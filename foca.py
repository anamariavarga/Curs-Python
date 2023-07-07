import xlsxwriter


def media(t: list) -> float:
    """Compute the average of values in the list
    :param t: a list with numbers
    :return: the average of the list numbers, rounded, with 2 decimals
    """

    if len(t) == 0:
        return 0
    return round(sum(t) / len(t), 2)


def get_catalog_from_file(file_name: str) -> dict:
    """Reads the catalog from a text file
    :rtype: object
    :param file_name: the name of the input file, txt with students names and grades
    :return:a dictionary { Students Names : their list of grades as integer }
    """

    ca = {}
    with open(file_name, 'r', encoding='utf-8') as catalog_file:
        for line in catalog_file:
            el = line.strip().split(';')
            ca[el[0]] = list(map(int, el[1:]))
    return ca


def create_final_catalog(c: dict, file_name: str):
    """Create the final catalog
    :param c: an input dictionary { Students Names : their grades as integer }
    :param file_name: a txt file created with the output dictionary { Students Names : their grades averages }
    """
    n, m, d = 25, 5, 2

    with open(file_name, 'w', encoding='utf-8') as cat_final:
        print(f'{"Nume":{n}} {"Prenume":{n}} {"Media":{m}} {"Note":>{m}}', file=cat_final)
        print('-' * (n + n + m + m + 3), file=cat_final)

        for elev, note in c.items():
            nume, prenume = elev.split()
            print(f'{nume:<{n}} {prenume:<{n}} {media(note):>{m}.{d}f} {len(note):^{m}}', file=cat_final)


def media_best(t: list, how_many: int = 3) -> float:
    """Compute the average of best how_many values in the list
    :param t: a list of grades
    :param how_many: describes how many grades to be considered in the average calculation (here are 3)
    :return: the grades average for each student (rounded integer with 2 decimals)
    """

    t = sorted(t, reverse=True)[:how_many]
    if len(t) == 0:
        return 0
    return round(sum(t) / len(t), 2)


def get_teze_from_file(file_name: str) -> dict:
    """Reads 'teze' from a file
    :param file_name: the file where 'teze' is read
    :return:a dictionary { Students Names : their grades from 'teze' file }
    """

    te = {}
    with open(file_name, 'r', encoding='utf-8') as teze:
        for line in teze:
            el = line.strip().split(';')
            te[el[0]] = int(el[1])
    return te


def create_final_catalog(c: dict, t: dict, file_name: str):
    """Create the final catalog
    :param c: a dictionary { Students Names : their grades }
    :param t: a dictionary { Students Names : their grades averages }
    :param file_name: a txt file with all students and their total average alphabetically sorted
    """

    n, m, d = 50, 2, 2

    with open(file_name, 'w', encoding='utf-8') as cat_final:
        header = f'{"Nume":{n}} {"Media":{m}}'
        print(header, file=cat_final)
        print('-' * len(header), file=cat_final)

        for el in sorted(c):
            media_total = media([media_best(c[el]), t[el]])
            print(f'{el:<{n}} {media_total:>{m}.{d}f}', file=cat_final)


def create_champions_catalog(c: dict, t: dict, file_name: str):
    """Creates the file with the champions
    :param c: a dictionary { Students Names : their grades }
    :param t: a dictionary { Students Names : their grades averages }
    :param file_name: a txt file with the first 3 students in descending order according to their total average
    """

    ch = {}
    for e, n in c.items():
        ch[e] = media([media_best(n), t[e]])

    n, m, d, p = 50, 2, 2, 6

    with open(file_name, 'w', encoding='utf-8') as cat_final:
        header = f'{"Premiu":{p}} {"Nume":{n}} {"Media":{m}}'
        print(header, file=cat_final)
        print('-' * len(header), file=cat_final)

        premiu = 1
        for el in sorted(ch, key=ch.get, reverse=True)[:3]:
            print(f"{premiu:^{p}} {el:{n}} {ch[el]:{m}.{d}f}", file=cat_final)
            premiu += 1


def create_unlucky_catalog(c: dict, t: dict, file_name: str):
    """Create the catalog with the unlucky ones
    :param c: a dictionary { Students Names : their grades }
    :param t: a dictionary { Students Names : their grades averages }
    :param file_name: a txt file with the students that didn't reach a total average >= 5
    """

    n, m, d = 50, 2, 2

    with open(file_name, 'w', encoding='utf-8') as cat_final:
        header = f'{"Nume":{n}} {"Media":{m}}'
        print(header, file=cat_final)
        print('-' * len(header), file=cat_final)

        for el in sorted(c):
            media_total = media([media_best(c[el]), t[el]])
            if media_total >= 5:
                continue
            print(f'{el:<{n}} {media_total:>{m}.{d}f}', file=cat_final)


#
# def sort_with_key_param(l: list) -> list:
#     """ Sort a list of strings according to int conversion
#     :rtype: list
#     :param l: an input list of strings
#     """
#     return sorted(l, key=int)
#
#
# def sum_of_tuples(t: list) -> list:
#     """Compute the sum of values in the list
#     :param t: a list of tuples
#     :return: an ascending sorted list of tuples by their own sum,, the sum is displayed
#     """
#     tup_sum = []
#     for i in t:
#         tup_sum.append(sum(i))

# def sum_element(element):
#     """Calculate the sum of elements for a list of tuples
#
#     :param element: each element from a tuple
#     :return: a list o tuples sorted ascending by the sum of the each tuple, the sum is not displayed, only the tuples
#     """
#     return sum(element)

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
