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

        user_id = request.args.get("user_id", type=int)

        query = """
            SELECT 
                u.name,
                we.workout_id,
                e.exercise_name,
                we.num_sets,
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
        """
        values = ()

        if user_id is not None:
            query += " WHERE w.user_id = %s"
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


@workout_bp.route("/workouts", methods=["POST"])
def add_workout():
    data = request.get_json() or {}

    required_fields = ["workout_id", "workout_date", "duration_minutes", "user_id"]
    for field in required_fields:
        if field not in data or data[field] in [None, ""]:
            return jsonify({"error": f"{field} is required"}), 400

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO Workout (workout_id, workout_date, duration_minutes, user_id)
            VALUES (%s, %s, %s, %s)
        """
        values = (
            int(data["workout_id"]),
            data["workout_date"],
            int(data["duration_minutes"]),
            int(data["user_id"])
        )

        cursor.execute(query, values)
        conn.commit()

        return jsonify({"message": "Workout added successfully"}), 201

    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"error": f"Failed to add workout: {str(e)}"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()