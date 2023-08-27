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
    q2 = 'select id from "Student";'
    c.execute(q2)
    records2 = c.fetchall()
    print(records2)
c=conn.cursor()
for record in records2:
        student_id = record[0]
        val = (student_id,)
        c.execute('''insert into Student_average (student_id) values (%s)''',val)
conn.commit()

c.close()
conn.close()
