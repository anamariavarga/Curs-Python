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
    q1 = '''select s.surname  as "Nume", s.first_name  as "Prenume",concat (c.class_no,c.class_letter)as Clasa
        from
            "Student" s
         join
            "Class" c on s."Class_id" = c.id
        order by "Nume"; '''
    c.execute(q1)
    records = c.fetchall()
    print(records)

c.close()
conn.close()
