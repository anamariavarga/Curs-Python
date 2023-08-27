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

n, m = 20, 5
fisier_text = 'output_17.2.txt'

with open(fisier_text, 'w', encoding='utf-8') as my_file:
    print(f'{"Nume":{n}} {"Prenume":{n}} {"Clasa":{m}}', file=my_file)
    print('-' * (n + n + m + 3), file=my_file)

    for record in records:
        print(f'{record[0]:<{n}} {record[1]:<{n}} {record[2]:>{m}}', file=my_file)

c.close()
conn.close()