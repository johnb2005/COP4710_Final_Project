from flask import Blueprint, jsonify, request
from backend.connection import get_connection

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/users", methods=["GET"])
def get_users():
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT user_id, name, email, age, join_date
            FROM Users
            ORDER BY user_id
        """
        cursor.execute(query)
        users = cursor.fetchall()

        for user in users:
            if user["join_date"] is not None:
                user["join_date"] = user["join_date"].strftime("%Y-%m-%d")
        return jsonify(users), 200

    except Exception as e:
        return jsonify({"error": f"Failed to fetch users: {str(e)}"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@user_bp.route("/users", methods=["POST"])
def add_user():
    conn = None
    cursor = None

    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Request body is required."}), 400

        user_id = data.get("user_id")
        name = str(data.get("name", "")).strip()
        email = str(data.get("email", "")).strip()
        age = data.get("age")
        join_date = data.get("join_date")

        if user_id is None:
            return jsonify({"error": "User ID is required."}), 400

        if not name:
            return jsonify({"error": "Name is required."}), 400

        if not email:
            return jsonify({"error": "Email is required."}), 400

        if age is None:
            return jsonify({"error": "Age is required."}), 400

        if join_date is None:
            return jsonify({"error": "Join date is required."}), 400

        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO Users (user_id, name, email, age, join_date)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (user_id, name, email, age, join_date)

        cursor.execute(query, values)
        conn.commit()

        return jsonify({"message": "User added successfully."}), 201

    except mysql.connector.IntegrityError as e:  # type: ignore
        return jsonify({"error": f"Database integrity error: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": f"Failed to add user: {str(e)}"}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


