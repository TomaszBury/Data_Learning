CREATE TABLE job_board (
  id SERIAL PRIMARY KEY,
  job TEXT,
  salary NUMERIC,
  salary_range numrange
);

INSERT INTO advanced_tutorial.public.job_board (job, salary, salary_range)
VALUES
  ('Engineer I', 120000, NUMRANGE(95000, 130000)),
  ('Engineer II', 150000, NUMRANGE(135000, 170000)),
  ('Engineer III', 210000, NUMRANGE(185000, 250000));

SELECT * FROM advanced_tutorial.public.job_board;

select  * from advanced_tutorial.public.job_board jb 
where jb.salary_range @> numrange(95000,95000, '[]');


drop table advanced_tutorial.public.job_board;

CREATE TABLE advanced_tutorial.public.job_board (
  id SERIAL PRIMARY KEY,
  job TEXT,
  salary NUMERIC,
  salary_numrange numrange,
  salary_intrange int4range
);

INSERT INTO advanced_tutorial.public.job_board (job, salary, salary_numrange, salary_intrange)
VALUES
  ('Engineer I', 120000, NUMRANGE(95000, 130000), INT4RANGE(95000, 130000)),
  ('Engineer II', 150000, NUMRANGE(135000, 170000), INT4RANGE(135000, 170000)),
  ('Engineer III', 210000, NUMRANGE(185000, 250000), INT4RANGE(185000, 250000));
  
 
SELECT * FROM advanced_tutorial.public.job_board;

select * from advanced_tutorial.public.job_board jb 
where salary_intrange @> 95000;