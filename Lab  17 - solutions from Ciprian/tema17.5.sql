create table student_average (
	id serial4 not null,
	average numeric not null,
	student_id int4 not null,
	primary key (id),
	foreign key (student_id) references public.student(id)
);

insert into student_average (average, student_id)
	select round(avg(grade), 2), student_id from grade group by student_id;