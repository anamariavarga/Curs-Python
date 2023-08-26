create table class (
	id serial primary key,
	class_number int,
	class_letter varchar(2)
);

create table student (
	id serial primary key,
	first_name varchar(20) not null,
	last_name varchar(20) not null,
	class_id int not null,
	foreign key (class_id) references class(id)
);

create table grade (
	id serial primary key,
	grade decimal not null,
	gdate date default current_date,
	student_id int not null,
	foreign key (student_id) references student(id)
);