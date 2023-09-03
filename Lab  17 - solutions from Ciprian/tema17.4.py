import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="palapa",
    password="palapa")


last_name = input('Introdu numele elevului:')
first_name = input('Introdu prenumele elevului:')

with conn:
    c = conn.cursor()
    query = """
        select
            s.id, 
            concat(c.class_number, c.class_letter) as "Clasa" 
        from student s
        join "class" c on s.class_id = c.id
        where s.first_name = %s and s.last_name = %s;
    """
    c.execute(query, (first_name, last_name))
    records = c.fetchone()
    if records:
        student_id = records[0]
        class_name = records[1]
        print(f'Elevul {last_name} {first_name} este in clasa {class_name}.')

        # %s::integer is useful to specify that the parameter is integer; but it can be omitted
        query = f"""
            select grade, gdate 
            from grade
            where student_id = %s::integer;
        """

        c.execute(query, (student_id,))
        record_grades = c.fetchall()
        if record_grades:
            print('Elevul are urmatoarele note in urmatoarele date:')
            for r in record_grades:
                print(r[0], r[1])
        else:
            print("Elevul nu are nicio nota.")
    else:
        print(f'Elevul {last_name} {first_name} nu se afla in baza de date.')

    c.close()

conn.close()
