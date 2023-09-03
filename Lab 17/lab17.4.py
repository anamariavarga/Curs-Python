import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="tema_lab16",
    user="postgres",
    password="Sofilica$9")

# c = conn.cursor()
# c.execute('select version()')
# db_version = c.fetchone()
# print('DB server version:', db_version)

student_fullname =input( 'Nume si prenume elev: ')
with conn, conn.cursor() as c:
    q1 = ''' select s.surname  as "Nume", s.first_name  as "Prenume",    
        concat (c.class_no,c.class_letter)as Clasa,
        g.grades as "Note",
        g.evaluation_date as "Data evaluare"
        FROM
            "Student" s
        JOIN
            "Grades" g ON g."Student_id" =s.id
        JOIN
            "Class" c ON s."Class_id"  = c.id;'''
    c.execute(q1)
    result = c.fetchall()
    print(result)
lista_elevi = []
lista_elevi = list(set([f'{item[0]} {item[1]}' for item in result]))
print(lista_elevi)


n, m = 20, 5
fisier_text2 = 'output_17.4.txt'
if student_fullname not in lista_elevi:
    print('Elevul: ' + student_fullname+ ' nu exista in lista elevilor')
else:
    with open(fisier_text2, 'w', encoding='utf-8') as my_file:
        print(f'{"Situatie elev: " + student_fullname:{2*n}} {"Clasa":{m}} {"Note":{m}} {"Data evaluare":{n}}',file=my_file)
        print('-' * (2*n + 2*m + n + 3), file=my_file)

        for elev in result:
            if f'{elev[0]} {elev[1]}' == student_fullname:
                output = f'{"":<{2*n}} {elev[2]:>{m}}  {elev[3]:^{m}}  {(elev[4]).isoformat():>{n}}'
                print(output, file=my_file)


c.close()
conn.close()
