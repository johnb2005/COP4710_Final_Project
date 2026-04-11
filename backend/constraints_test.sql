--1) Constraint Test Cases for USERS Table (email NOT NULL)
INSERT INTO USERS (user_id, name, email, age, join_date)
VALUES (20, ' User', NULL, 25, '2024-01-01');
--Error Message: ERROR 1048 (23000): Column 'email' cannot be null

--2) Constraint Test Cases for USERS Table(email UNIQUE)
INSERT INTO USERS (user_id, name, email, age, join_date)
VALUES (22, 'Bob Test', 'alice@test.com', 30, '2024-01-02');
--Error Message: ERROR 1062 (23000): Duplicate entry 

--3) Constraint Test Cases for USERS Table(age > 0)
INSERT INTO USERS (user_id, name, email, age, join_date)
VALUES (30, 'Invalid User', 'invalid@test.com', -5, '2024-01-01');
--ERROR 3819 (HY000): Check constraint 'chk_age_positive' is violated.

--4) Constraint Test Cases for WORKOUT Table(duration_minutes between 0 and 1440)
INSERT INTO WORKOUT (workout_id, workout_date, duration_minutes, user_id)
VALUES (2001, '2024-01-01', 1500, 5);
--ERROR 3819 (HY000): Check constraint 'chk_duration_range' is violated.

--5) Constraint Test Cases for GOAL Table(start_date < end_date)
INSERT INTO GOAL (goal_id, user_id, metric_type, current_value, target_value, start_date, end_date)
    -> VALUES (1, 5, 'Weight Loss', 180, 160, '2024-05-01', '2024-04-01');
--ERROR 3819 (HY000): Check constraint 'chk_goal_dates' is violated.