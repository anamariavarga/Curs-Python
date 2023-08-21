query_start = "insert into student (surname,first_name,class_nr,class_letter,birth_date,average_grade) values ('"

first_line = True
with open('student.csv') as csv, open('tema15.2.sql', 'w') as insert:
    for line in csv:
        if first_line:
            first_line = False
            continue
        values = line.strip().split(',')
        query = query_start + "','".join(values) + "');"
        print(query, file=insert)


