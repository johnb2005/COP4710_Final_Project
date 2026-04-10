 

CREATE TABLE EXERCISE(
    exercise_id INT NOT NULL,
    exercise_name VARCHAR(100),
    muscle_group VARCHAR(50),
    equipment VARCHAR(50),
    PRIMARY KEY (exercise_id)
);

CREATE TABLE GOAL(
    goal_id INT NOT NULL,
    user_id INT,
    metric_type VARCHAR(50),
    current_value DECIMAL(6,2),
    target_value DECIMAL(6,2),
    start_date DATE,
    end_date DATE,
    PRIMARY KEY (goal_id),
    FOREIGN KEY (user_id)
        REFERENCES USER(user_id)
        ON DELETE CASCADE
);

CREATE TABLE USER(
    user_id INT NOT NULL,
    name VARCHAR(100),
    email VARCHAR(255),
    age INT,
    join_date DATE,
    PRIMARY KEY (user_id)
);

CREATE TABLE WORKOUT(
    workout_id INT NOT NULL,
    workout_date DATE,
    duration_minutes INT,
    user_id INT,
    PRIMARY KEY (workout_id),
    FOREIGN KEY (user_id)
        REFERENCES USER(user_id)
        ON DELETE CASCADE
);

CREATE TABLE WORKOUT_EXERCISE(
    workout_id INT NOT NULL,
    exercise_id INT NOT NULL,
    sets INT,
    reps INT,
    weight_used DECIMAL(6,2),
    time_spent INT,
    difficulty_level VARCHAR(20),
    PRIMARY KEY (workout_id, exercise_id),
    FOREIGN KEY (workout_id)
        REFERENCES WORKOUT(workout_id)
        ON DELETE CASCADE,
    FOREIGN KEY (exercise_id)
        REFERENCES EXERCISE(exercise_id)
        ON DELETE CASCADE
);