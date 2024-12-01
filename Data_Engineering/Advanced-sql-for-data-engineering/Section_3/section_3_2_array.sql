CREATE TABLE array_table (
  id SERIAL PRIMARY KEY,
  myarray INTEGER[]
);

-- Create an ARRAY column
select * from 
array_table ;

insert into array_table (myarray)
values (array[1, 2, 3, 4]);

select * from 
array_table ;


-- Querying an ARRAY column
SELECT *
FROM array_table
WHERE 2 = ANY(myarray);


insert into array_table (myarray)
values (array[9, 27, 43, 64]);

select * 
from array_table 
where array[9, 27, 43, 64]::integer[] = myarray;

-- Unpivot an ARRAY column
select id, unnest(myarray)
from array_table ;