CREATE TABLE advanced_tutorial.public.employees ( id SERIAL PRIMARY KEY, 
name VARCHAR (255), 
salary NUMERIC, 
department VARCHAR (255), 
bonus NUMERIC
);


drop table advanced_tutorial.public.employees ;

INSERT INTO advanced_tutorial.public.employees (name, salary, department, bonus) VALUES
	('John Doe', 50000.00, 'IT', 5000),
	('Jane Doe', NULL, 'Sales', 5000),
	('Bob Smith', 55000.00, NULL, 5000);


select 
		name,
		salary,
		case
			when salary < 60000 then 'entry level'
			when salary < 100000 then 'mid'
			when salary < 200000 then 'big baller'
			when salary < 200000 or bonus > 0 then 'really big baller'
			else 'uncaught exception'
	end as salary_classification
from
	advanced_tutorial.public.employees ;