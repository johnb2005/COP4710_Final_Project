-- Query 1 Multi table join
SELECT
    u.name,
    we.workout_id,
    e.exercise_name,
    we.sets,
    we.reps,
    we.weight_used,
    we.time_spent
FROM WorkoutExercise we
JOIN ExerciseLibrary e
    ON we.exercise_id = e.exercise_id
JOIN Workout w
    ON we.workout_id = w.workout_id
JOIN Users u
    ON w.user_id = u.user_id
WHERE u.user_id = 1
ORDER BY we.workout_id, e.exercise_name;


-- Query 2 GROUP BY with aggregation
SELECT
    u.user_id AS User_id,
    u.name AS Name,
    COUNT(w.workout_id) AS Number_Of_Workouts,
    SUM(w.duration_minutes) AS Time_Spent_Working_Out
FROM Users u
JOIN Workout w
    ON u.user_id = w.user_id
GROUP BY u.user_id, u.name
ORDER BY u.user_id;

-- Query 3 Where subquery 
SELECT
    u.user_id,
    u.name
FROM Users u
WHERE u.user_id IN (
    SELECT user_id
    FROM Workout
    GROUP BY user_id
    HAVING COUNT(*) > (
        SELECT AVG(workout_count)
        FROM (
            SELECT COUNT(*) AS workout_count
            FROM Workout
            GROUP BY user_id
        ) AS counts
    )
)
ORDER BY u.user_id;

-- Query 4 CASE
SELECT
    u.name,
    u.user_id,
    g.metric_type,
    g.current_value,
    g.target_value,
    CASE
        WHEN g.metric_type IN ('Bench Press 1RM (kg)')
             AND g.current_value >= g.target_value
        THEN 'Met Goal'
        WHEN g.metric_type IN ('Weight Loss (kg)', 'Body Fat (%)', '5K Time (min)')
             AND g.current_value <= g.target_value
        THEN 'Met Goal'
        ELSE 'Not Met'
    END AS goal_status
FROM Users u
JOIN Goal g
    ON u.user_id = g.user_id
ORDER BY u.user_id;

-- Query 5 Multiple conditions filter
SELECT
    u.name,
    we.workout_id,
    e.exercise_name,
    we.sets,
    we.reps,
    we.weight_used,
    we.time_spent
FROM WorkoutExercise we
JOIN ExerciseLibrary e
    ON we.exercise_id = e.exercise_id
JOIN Workout w
    ON we.workout_id = w.workout_id
JOIN Users u
    ON w.user_id = u.user_id
WHERE w.user_id = 1
ORDER BY we.workout_id, e.exercise_name;

-- Query 6 INSERT
INSERT INTO ExerciseLibrary (exercise_id, exercise_name, muscle_group, equipment)
VALUES (109, 'Hammer Curl', 'Arms', 'Dumbbells');

-- Query 7 UPDATE
UPDATE Goal
SET current_value = 26.50
WHERE user_id = 1;

-- Query 8 DELETE 
DELETE FROM ExerciseLibrary
WHERE exercise_id = 109;
