INSERT INTO USERS (user_id, name, email, age, join_date) VALUES
(5, 'Alice Johnson', 'alice.johnson@example.com', 28, '2024-01-15'),
(6, 'Brian Smith', 'brian.smith@example.com', 34, '2023-11-22'),
(7, 'Catherine Lee', 'catherine.lee@example.com', 25, '2024-03-10'),
(8, 'David Brown', 'david.brown@example.com', 40, '2022-09-05'),
(9, 'Emily Davis', 'emily.davis@example.com', 31, '2023-06-18'),
(10, 'Frank Wilson', 'frank.wilson@example.com', 29, '2024-02-27');

INSERT INTO GOAL (goal_id, user_id, metric_type, current_value, target_value, start_date, end_date) VALUES
(1, 5, 'Weight Loss', 180.00, 150.00, '2024-01-15', '2024-06-15'),
(2, 6, 'Muscle Gain', 160.00, 180.00, '2023-11-22', '2024-05-22'),
(3, 7, 'Endurance', 30.00, 60.00, '2024-03-10', '2024-09-10'),
(4, 8, 'Flexibility', 20.00, 40.00, '2022-09-05', '2023-03-05'),
(5, 9, 'Cardio Fitness', 15.00, 30.00, '2023-06-18', '2023-12-18'),
(6, 10, 'Strength Training', 100.00, 150.00, '2024-02-27', '2024-08-27');

INSERT INTO EXERCISELIBRARY (exercise_id, exercise_name, muscle_group, equipment) VALUES
(108, 'Squat', 'Legs', 'Barbell'),
(109, 'Bench Press', 'Chest', 'Barbell'),
(110, 'Deadlift', 'Back', 'Barbell'),
(111, 'Overhead Press', 'Shoulders', 'Dumbbell'),
(112, 'Bicep Curl', 'Arms', 'Dumbbell'),
(113, 'Tricep Extension', 'Arms', 'Cable Machine');   

INSERT INTO WORKOUT (workout_id, workout_date, duration_minutes, user_id) VALUES
(1006, '2024-01-20', 60, 5),
(1007, '2024-01-22', 45, 6),
(1008, '2024-01-25', 30, 7),
(1009, '2024-01-28', 50, 8),
(1010, '2024-01-30', 40, 9),
(1011, '2024-02-02', 55, 10);

INSERT INTO WORKOUTEXERCISE (workout_id, exercise_id, `sets`, reps, weight_used, time_spent, difficulty_level) VALUES
(1006, 108, 4, 10, 100.00, 20, 'Intermediate'),
(1006, 109, 3, 8, 80.00, 15, 'Beginner'),
(1007, 110, 5, 5, 150.00, 25, 'Advanced'),
(1007, 111, 4, 12, 40.00, 20, 'Intermediate'),
(1008, 112, 3, 15, 20.00, 10, 'Beginner'),
(1008, 113, 4, 10, 30.00, 15, 'Intermediate'),
(1009, 108, 5, 8, 110.00, 25, 'Advanced'),
(1009, 109, 4, 10, 90.00, 20, 'Intermediate'),
(1010, 110, 3, 6, 140.00, 30, 'Advanced'),
(1010, 111, 4, 12, 50.00, 20,'Intermediate'),
(1011 ,112 ,5 ,15 ,25.00 ,10 , 'Beginner'),
(1011 ,113 ,4 ,10 ,35.00 ,15 , 'Intermediate');





