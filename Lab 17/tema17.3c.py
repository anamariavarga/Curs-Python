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
    q1 = '''select count(*)from "Student" s , "Class" c
        where s."Class_id"=c.id and c.class_letter like 'B';'''
    c.execute(q1)
    records = c.fetchone()
    print(records[0])

c.close()
conn.close()
