# Project: 0x0D. SQL - Introduction

## Resources

#### Read or watch:

* [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
* [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
* [Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
* [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
* [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
* [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
* [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
* [installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)
## Learning Objectives

### General

* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does <code>DDL</code> and <code>DML</code> stand for
* How to <code>CREATE</code> or <code>ALTER</code> a table
* How to <code>SELECT</code> data from a table
* How to <code>INSERT</code>, <code>UPDATE</code> or <code>DELETE</code> data
* What are <code>subqueries</code>
* How to use MySQL functions
## Tasks


* **0. List databases**
  * [0-list_databases.sql](./0-list_databases.sql): Lists all databases of your MySQL server.

* **1. Create a database**
  * [1-create_database_if_missing.sql](./1-create_database_if_missing.sql): Creates the database `hbtn_0c_0` in your MySQL server.
    * If the database `hbtn_0c_0` already exists, your script should not fail.
    * You are not allowed to use the `SELECT` or `SHOW` statements.

* **2. Delete a database**
  * [2-remove_database.sql](./2-remove_database.sql): Deletes the database `hbtn_0c_0` in your MySQL server.
    * If the database `hbtn_0c_0` already exists, your script should not fail.
    * You are not allowed to use the `SELECT` or `SHOW` statements.

* **3. List tables**
  * [3-list_tables.sql](./3-list_tables.sql): Lists all the tables of a database in your MySQL server.

* **4. First table**
  * [4-first_table.sql](./4-first_table.sql): Creates a table called `first_table` in the current database in your MySQL server.
    * `first_table` description:
      * `id` INT
      * `name` VARCHAR(256)
    * The database name will be passed as an argument of the mysql command.
    * If the table `first_table` already exists, your script should not fail.
    * You are not allowed to use the `SELECT` or SHOW statements.

* **5. Full description**
  * [5-full_table.sql](./5-full_table.sql): Prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
    * You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements.

* **6. List all in table** 
  * [6-list_values.sql](./6-list_values.sql): Lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
 
* **7. First add**
  * [7-insert_value.sql](./7-insert_value.sql): Inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
    * New row:
      * `id` = 89
      * `name` = Best School

* **8. Count 89**
  * [8-count_89.sql](./8-count_89.sql): Displays the number of records with `id` = 89 in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

* **9. Full creation**
  * [9-full_creation.sql](./9-full_creation.sql): Creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.
    * `second_table` description:
      * `id` INT
      * `name` VARCHAR(256)
      * `score` INT
    * If the table second_table already exists, your script should not fail.
    * You are not allowed to use the `SELECT` and `SHOW` statements.
    * Your script should create these records:
      * `id` = 1, `name` = “John”, `score` = 10
      * `id` = 2, `name` = “Alex”, `score` = 3
      * `id` = 3, `name` = “Bob”, `score` = 14
      * `id` = 4, `name` = “George”, `score` = 8

* **10. List by best**
  * [10-top_score.sql](./10-top_score.sql): Lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
    * Results should display both the score and the name (in this order).
    * Records should be ordered by score (top first).
    * The database name will be passed as an argument of the `mysql` command.

* **11. Select the best**
  * [11-best_score.sql](./11-best_score.sql): Lists all records with a `score` >= 10 in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
    * Results should display both the score and the name (in this order).
    * Records should be ordered by score (top first).
    * The database name will be passed as an argument of the `mysql` command.

* **12. Cheating is bad**
  * [12-no_cheating.sql](./12-no_cheating.sql): Updates the score of Bob to `10` in the table `second_table`.
    * You are not allowed to use Bob’s id value, only the `name` field.
    * The database name will be passed as an argument of the `mysql` command.

* **13. Score too low**
  * [13-change_class.sql](./13-change_class.sql): Removes all records with a `score` <= 5 in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
    * The database name will be passed as an argument of the `mysql` command.

* **14. Average**
  * [14-average.sql](./14-average.sql): computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
    * The result column name should be `average`.
    * The database name will be passed as an argument of the `mysql` command.

* **15. Number by score**
  * [15-groups.sql](./15-groups.sql): Lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
    * The result should display:
      * the `score`
      * the number of records for this `score` with the label `number`
    * The list should be sorted by the number of records (descending).
    * The database name will be passed as an argument of the `mysql` command.


* **16. Say my name**
  * [16-no_link.sql](./16-no_link.sql): Lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
    * Don’t list rows without a `name` value.
    * Results should display the `score` and the `name` (in this order).
    * Records should be listed by descending score.
    * The database name will be passed as an argument of the `mysql` command.

* **17. Go to UTF8**
  * [100-move_to_utf8.sql](./100-move_to_utf8.sql): Converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, `collate utf8mb4_unicode_ci`) in your MySQL server.
    * You need to convert all of the following to UTF8:
      * Database `hbtn_0c_0`
      * Table `first_table`
      * Field `name` in `first_table`


* **18. Temperatures #0**
  * [101-avg_temperatures.sql](./101-avg_temperatures.sql): Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
    * Import in `hbtn_0c_0` database [this](./temperatures.sql) table dump.

* **19. Temperatures #1**
  * [102-top_city.sql](./102-top_city.sql): displays the top 3 of cities temperature during July and August ordered by temperature (descending)
    * Import in `hbtn_0c_0` database [this](./temperatures.sql) table dump.

* **20. Temperatures #2**
  * [103-max_state.sql](./103-max_state.sql): Displays the max temperature of each state (ordered by State name).
    * Import in `hbtn_0c_0` database [this](./temperatures.sql) table dump.