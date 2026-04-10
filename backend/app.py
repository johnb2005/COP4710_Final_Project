from flask import Flask
from backend.routes.users import user_bp
from backend.routes.user_workouts import workout_bp
from backend.routes.workout_stats import workout_stats
from backend.routes.user_goals import user_goal_info

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(workout_bp)
app.register_blueprint(workout_stats)
app.register_blueprint(user_goal_info)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
