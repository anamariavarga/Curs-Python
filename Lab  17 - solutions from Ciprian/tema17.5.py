import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="mydb",
        user="palapa",
        password="palapa")


def create_average_table():
    global conn
    query = """
        drop table if exists student_average;
        create table student_average (
            id serial4 not null,
            average numeric not null,
            student_id int4 not null,
            primary key (id),
            foreign key (student_id) references public.student(id)
            );
    """
    with conn:
        c = conn.cursor()
        c.execute(query)
        c.close()


def get_student_ids() -> list:
    """Get the ids of the students that have grades"""
    global conn
    query = "select distinct(student_id) from grade;"
    c = conn.cursor()
    c.execute(query)
    ret = []
    for t, in c.fetchall():
        ret += [t]
    return ret


def get_averages(ids) -> dict:
    global conn
    c = conn.cursor()
    query = "select grade from grade where student_id = %s::integer"
    ret = {}
    for i in ids:
        s = 0
        c.execute(query, (i, ))
        grades = c.fetchall()
        for g, in grades:
            s += g
        ret[i] = round(float(s / len(grades)), 2)

    return ret


def insert_averages(av: dict):
    """Inserts averages in the table"""
    global conn
    with conn:
        c = conn.cursor()
        query = "insert into student_average (average, student_id) values (%s::float, %s::integer);"
        for k, v in av.items():
            c.execute(query, (v, k))
        c.close()


def display_averages():
    query = """
        select s.first_name, s.last_name, sa.average 
        from student s, student_average sa
        where s.id = sa.student_id
        order by sa.average desc;
    """
    c = conn.cursor()
    c.execute(query)
    for n, p, a in c.fetchall():
        print(f'{n} {p} - {a}')
    c.close()


if __name__ == '__main__':
    conn = get_connection()
    create_average_table()
    student_ids = get_student_ids()
    averages = get_averages(student_ids)
    insert_averages(averages)
    display_averages()
    conn.close()
