# Write your MySQL query statement below
SELECT Max(salary) AS SecondHighestSalary
FROM employee 
WHERE salary NOT IN (SELECT MAX(salary) FROM employee)
