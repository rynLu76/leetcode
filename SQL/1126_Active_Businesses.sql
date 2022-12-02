Table: Events

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| business_id   | int     |
| event_type    | varchar |
| occurences    | int     | 
+---------------+---------+
(business_id, event_type) is the primary key of this table.
Each row in the table logs the info that an event of some type occurred at some business for a number of times.
 

The average activity for a particular event_type is the average occurences across all companies that have this event.

An active business is a business that has more than one event_type such that their occurences is strictly greater than the average activity for that event.

Write an SQL query to find all active businesses.



----------------------------------------------------------------------
select e2.business_id
from
(
  select event_type, avg(occurences) as avg_occ
  from events
  group by event_type
) as e1
join events e2
on e1.event_type = e2.event_type
and e2.occurences > e1.occurences
group by business_id
having count(distinct e1.event_type) > 1;
----------------------------------------------------------------------



Input: 
Events table:
+-------------+------------+------------+
| business_id | event_type | occurences |
+-------------+------------+------------+
| 1           | reviews    | 7          |
| 3           | reviews    | 3          |
| 1           | ads        | 11         |
| 2           | ads        | 7          |
| 3           | ads        | 6          |
| 1           | page views | 3          |
| 2           | page views | 12         |
+-------------+------------+------------+
Output: 
+-------------+
| business_id |
+-------------+
| 1           |
+-------------+
