import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="palapa",
    password="palapa")


with conn:
    query = """
        select 
            s.last_name as "Nume", s.first_name as "Prenume", 
            concat(c.class_number, c.class_letter) as "Clasa" 
        from student s
        join "class" c on s.class_id = c.id 
        order by s.last_name;
    """
    c = conn.cursor()
    c.execute(query)

    records = c.fetchall()

    with open('tema17.2.txt', 'w') as file:
        print(f"{'Nume':20} {'Prenume':20} {'Clasa':5}", file=file)
        print('-' * 47, file=file)
        for r in records:
            print(f'{r[0]:20} {r[1]:20} {r[2]:>5}', file=file)

    c.close()

conn.close()
