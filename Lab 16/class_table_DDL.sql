-- public.class_table definition

-- Drop table

-- DROP TABLE public.class_table;

CREATE TABLE public.class_table (
	id serial4 NOT NULL,
	class_no varchar(20) NOT NULL,
	class_letter varchar(20) NOT NULL,
	description varchar(100) NULL,
	CONSTRAINT class_table_pkey PRIMARY KEY (id)
);