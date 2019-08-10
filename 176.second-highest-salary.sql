--
-- @lc app=leetcode id=176 lang=mysql
--
-- [176] Second Highest Salary
--
-- https://leetcode.com/problems/second-highest-salary/description/
--
-- database
-- Easy (27.90%)
-- Total Accepted:    145.3K
-- Total Submissions: 521K
-- Testcase Example:  '{"headers": {"Employee": ["Id", "Salary"]}, "rows": {"Employee": [[1, 100], [2, 200], [3, 300]]}}'
--
-- Write a SQL query to get the second highest salary from the Employee
-- table.
-- 
-- 
-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- 
-- 
-- For example, given the above Employee table, the query should return 200 as
-- the second highest salary. If there is no second highest salary, then the
-- query should return null.
-- 
-- 
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+
-- 
-- 
--
# Write your MySQL query statement below
-- SELECT
--     MAX(B.Salary) AS 'SecondHighestSalary'
-- FROM (
--     SELECT
--         A.Salary,
--         RANK() OVER (
--             ORDER BY Salary DESC
--         ) AS RANKING
--     FROM Employee A
--     ) B
-- HAVING B.RANKING > 1

select 
MAX(C.Salary) AS "SecondHighestSalary"
FROM(
select 
@rownum := @rownum + 1 as ROWNUM, A.*
from (select Distinct Salary from Employee order by Salary desc) A
,(select @rownum :=0) B
) c
WHERE ROWNUM > 1

-- select Salary as SecondHighestSalary from Employee order by Salary desc limit 1 offset 1
