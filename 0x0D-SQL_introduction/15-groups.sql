-- script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0
-- The result should display:the scorethe number of records for this score with the label number
-- The list should be sorted by the number of records (descending)
-- Execute with cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
