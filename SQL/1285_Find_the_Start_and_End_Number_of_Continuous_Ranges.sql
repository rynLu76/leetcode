Table: Logs

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| log_id        | int     |
+---------------+---------+
log_id is the primary key for this table.
Each row of this table contains the ID in a log Table.
 

Write an SQL query to find the start and end number of continuous ranges in the table Logs.



----------------------------------------------------------------------
select min(log_id) as start_id, max(log_id) as end_id
(
  select log_id, row_number() over(order by log_id) as nums
  from Logs
) as a
group by log_id - num;
----------------------------------------------------------------------



Input: 
Logs table:
+------------+
| log_id     |
+------------+
| 1          |
| 2          |
| 3          |
| 7          |
| 8          |
| 10         |
+------------+
Output: 
+------------+--------------+
| start_id   | end_id       |
+------------+--------------+
| 1          | 3            |
| 7          | 8            |
| 10         | 10           |
+------------+--------------+
