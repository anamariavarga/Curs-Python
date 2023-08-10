import csv

csv_file = 'student (1).csv'
sql_file = 'tema15.2.sql'

with open(csv_file, 'r', newline='', encoding='iso-8859-1') as csvfile, open(sql_file, 'w', encoding='utf-8') as sqlfile:

    csvreader = csv.reader(csvfile, delimiter=' ')

    next(csvreader)  # Ignorăm prima linie (antetul)
    for column in csvreader:
        print("Column:", column)

        if len(column) < 6:
            print("Skipping incomplete row:", column)
            continue
        surname = column[0]
        first_name = column[1]
        class_nr = column[2]
        class_letter = column[3]
        birth_date = column[4]
        average_grade = column[5]

        sql_query = f"insert into student (surname, first_name, class_nr, class_letter, birth_date, average_grade)\n"
        sql_query += f"values ('{surname}', '{first_name}', '{class_nr}', '{class_letter}', '{birth_date}', '{average_grade}');\n"
        sql_query += "1\n\n"

        sqlfile.write(sql_query)
