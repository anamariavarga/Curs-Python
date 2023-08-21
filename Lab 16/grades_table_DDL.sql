-- public.grades_table definition

-- Drop table

-- DROP TABLE public.grades_table;

CREATE TABLE public.grades_table (
	id serial4 NOT NULL,
	evaluation_date date NULL DEFAULT CURRENT_DATE,
	istorie varchar(10) NULL,
	fizica varchar(10) NULL,
	romana varchar(10) NULL,
	info varchar(10) NULL,
	student_table_id int4 NULL,
	class_table_id int4 NULL,
	CONSTRAINT grades_table_pkey PRIMARY KEY (id),
	CONSTRAINT grades_table_class_table_id_fkey FOREIGN KEY (class_table_id) REFERENCES public.class_table(id),
	CONSTRAINT grades_table_student_table_id_fkey FOREIGN KEY (student_table_id) REFERENCES public.student_table(id)
);