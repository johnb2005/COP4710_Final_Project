from flask import Blueprint, jsonify, request
from backend.connection import get_connection

user_goal_info = Blueprint("user_goal_info",__name__)

@user_goal_info.route("/user_goal_info",methods=["GET"])
def get_user_goal_info():
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)


        query = """
        
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

        
        WHEN g.metric_type IN ('Weight Loss (kg)', 'Body Fat (%)','5K Time (min)')
             AND g.current_value <= g.target_value
        THEN 'Met Goal'

        ELSE 'Not Met'
    END AS goal_status
FROM Users u
JOIN Goal g
    ON u.user_id = g.user_id;
        
        
        """

        cursor.execute(query)
        goal_info = cursor.fetchall()

        return jsonify(goal_info),200

    except Exception as e:
        return jsonify({"error": f"Failed to fetch workouts: {str(e)}"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


