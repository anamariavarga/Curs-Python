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
with conn, conn.cursor() as c:
    q1 = ''' select s.surname  as "Nume", s.first_name  as "Prenume",    
        g.grades as "Note"
        FROM
            "Student" s
        JOIN
            "Grades" g ON g."Student_id" =s.id;'''
    c.execute(q1)
    records = c.fetchall()
    print(records)
lista_elevi = []
lista_elevi = list(set([f'{item[0]} {item[1]}' for item in records]))
# print(lista_elevi)
catalog = {}

for surname, first_name, grades in records:
    full_name = f"{surname} {first_name}"
    grades = float(grades)

    if full_name in catalog:
        catalog[full_name].append(grades)
    else:
        catalog[full_name] = [grades]

for full_name, grades in catalog.items():
    average = round(sum(grades) / len(grades), 2)
    print(f" {full_name}: {average:.2f}")
    c = conn.cursor()
    val = (average,)
    query = 'insert into Student_average (average) values(%s)'
    c.execute(query, val)
    conn.commit()

c.close()
conn.close()