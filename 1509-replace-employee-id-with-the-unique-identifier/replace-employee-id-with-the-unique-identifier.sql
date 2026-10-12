select eu.unique_id, em.name as name 
from employees em
left join EmployeeUNI eu
on em.id = eu.id;