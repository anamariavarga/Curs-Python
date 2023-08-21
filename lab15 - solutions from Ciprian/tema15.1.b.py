query_start = "insert into student (surname,first_name,class_nr,class_letter,birth_date,average_grade) values ('"

with open('student.csv') as csv, open('tema15.2.sql', 'w') as insert:
    all_rows = csv.readlines()
    for line in all_rows[1:]:
        values = line.strip().split(',')
        query = query_start + "','".join(values) + "');"
        print(query, file=insert)


