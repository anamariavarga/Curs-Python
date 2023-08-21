-- public.student_table definition

-- Drop table

-- DROP TABLE public.student_table;

CREATE TABLE public.student_table (
	id serial4 NOT NULL,
	surname varchar(20) NOT NULL,
	first_name varchar(20) NOT NULL,
	class_table_id int4 NULL,
	CONSTRAINT student_table_pkey PRIMARY KEY (id),
	CONSTRAINT student_table_class_table_id_fkey FOREIGN KEY (class_table_id) REFERENCES public.class_table(id)
);