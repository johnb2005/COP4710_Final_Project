from flask import Blueprint, jsonify, request
from backend.connection import get_connection

user_goal_info = Blueprint("user_goal_info", __name__)


@user_goal_info.route("/user_goal_info", methods=["GET"])
def get_user_goal_info():
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        user_id = request.args.get("user_id", type=int)

        query = """
            SELECT
                u.name,
                u.user_id,
                g.metric_type,
                g.current_value,
                g.target_value,
                CASE
                    WHEN g.metric_type = 'Bench Press 1RM (kg)'
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
        """
        values = ()

        if user_id is not None:
            query += " WHERE u.user_id = %s"
            values = (user_id,)

        cursor.execute(query, values)
        goal_info = cursor.fetchall()

        return jsonify(goal_info), 200

    except Exception as e:
        return jsonify({"error": f"Failed to fetch goals: {str(e)}"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@user_goal_info.route("/goals", methods=["POST"])
def add_goal():
    data = request.get_json() or {}

    required_fields = [
        "goal_id",
        "user_id",
        "metric_type",
        "current_value",
        "target_value",
        "start_date",
        "end_date"
    ]

    for field in required_fields:
        if field not in data or data[field] in [None, ""]:
            return jsonify({"error": f"{field} is required"}), 400

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO Goal (
                goal_id, user_id, metric_type, current_value,
                target_value, start_date, end_date
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            int(data["goal_id"]),
            int(data["user_id"]),
            data["metric_type"],
            float(data["current_value"]),
            float(data["target_value"]),
            data["start_date"],
            data["end_date"]
        )

        cursor.execute(query, values)
        conn.commit()

        return jsonify({"message": "Goal added successfully"}), 201

    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"error": f"Failed to add goal: {str(e)}"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()