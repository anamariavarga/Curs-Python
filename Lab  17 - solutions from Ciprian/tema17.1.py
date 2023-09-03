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
    print(records, type(records))

    for r in records:
        print(r)
    c.close()

conn.close()
