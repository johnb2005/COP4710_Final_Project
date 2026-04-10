from flask import Blueprint, jsonify, request
from backend.connection import get_connection

workout_bp = Blueprint("workout_bp", __name__)


@workout_bp.route("/user-workouts", methods=["GET"])
def get_user_workouts():
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        user_id = request.args.get("user_id")

        query = """
            SELECT 
                u.name,
                w.workout_id,
                e.exercise_name,
                w.sets,
                w.reps,
                w.weight_used,
                w.time_spent
            FROM WorkoutExercise w
            JOIN ExerciseLibrary e
                ON w.exercise_id = e.exercise_id
            JOIN Workout
                ON w.workout_id = Workout.workout_id
            JOIN Users u
                ON Workout.user_id = u.user_id
        """

        values = ()

        if user_id:
            query += " WHERE Workout.user_id = %s"
            values = (user_id,)

        cursor.execute(query, values)
        workouts = cursor.fetchall()

        return jsonify(workouts), 200

    except Exception as e:
        return jsonify({"error": f"Failed to fetch workouts: {str(e)}"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()