from flask import Blueprint, jsonify, request
from backend.connection import get_connection

workout_stats = Blueprint("workout_stats",__name__)

@workout_stats.route("/workout_stats",methods=["GET"])
def get_workout_stats():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)


        query = """
        SELECT u.user_id AS User_id, u.name AS Name, COUNT(workout_id) AS Number_Of_Workouts,SUM(duration_minutes) AS Time_Spent_Working_Out
        FROM Users u
        JOIN Workout w
        ON u.user_id = w.user_id
        GROUP BY u.user_id,u.name;
        """

        cursor.execute(query)
        workout_statistics = cursor.fetchall()

        return jsonify(workout_statistics), 200

    except Exception as e:
        return jsonify({"error": f"Failed to fetch workouts: {str(e)}"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


