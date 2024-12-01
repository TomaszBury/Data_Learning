create table class_unnormalized (
	student_id serial,
	advisor varchar,
	room varchar,
	class1 varchar,
	class2 varchar,
	class3 varchar
);
insert into advanced_tutorial.public.class_unnormalized (
	advisor,
	room,
	class1,
	class2,
	class3
)
values
('Jones', 123, 'Biology', 'Chemistry', 'Physics'),
('Smith', 131, 'English', 'Math', 'Library Science');


select * from advanced_tutorial.public.class_unnormalized;



select c.student_id, t.*
from advanced_tutorial.public.class_unnormalized c
  cross join lateral (
     values 
       (c.class1, 'class1'),
       (c.class2, 'class2'),
       (c.class3, 'class3')
  ) as t --(subject, class_num)
order by student_id;