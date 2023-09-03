select count(*) from student;

select count(*) from student where last_name = 'Popescu';

select count(s.last_name)
from student s
join "class" c on c.id = s.class_id
where c.class_number = 8 and c.class_letter = 'b';