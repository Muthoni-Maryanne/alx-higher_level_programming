-- script that updates the score of Bob to 10 in the table second_table
-- Not allowed to use Bob’s id value, only the name field
-- Execute with cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- Then show table after with cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
UPDATE second_table SET score = 10 WHERE name = "Bob";
