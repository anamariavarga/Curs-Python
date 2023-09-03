select
	s.last_name as "Nume", s.first_name as "Prenume",
	concat(c.class_number, c.class_letter) as "Clasa"
from student s
join "class" c on s.class_id = c.id
order by s.last_name;
