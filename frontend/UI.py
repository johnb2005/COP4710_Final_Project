import streamlit as st
import requests
import pandas as pd

API_BASE_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="PantherFitness Database", layout="centered")

st.title("PantherFitness Database")

tab1,tab2,tab3,tab4 = st.tabs(["Users","Workouts","Workout Statistics","User Goals"])

with tab1:
    st.subheader("Users Table")

    try:
        response = requests.get(f"{API_BASE_URL}/users", timeout=5)

        if response.status_code == 200:
            users = response.json()
            df = pd.DataFrame(users)


            if not df.empty:
                df = df[["user_id", "name", "email", "age", "join_date"]]
                df = df.reset_index(drop=True)

            st.data_editor(
                df,
                use_container_width=True,
                hide_index=True
            )



        else:
            try:
                error_json = response.json()
                st.error(f"Failed to fetch users: {error_json.get('error', 'Unknown error')}")
            except Exception:
                st.error("Failed to fetch users.")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the Flask API. Make sure backend/app.py is running.")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")

    with st.expander("Add New User"):
        user_id = st.number_input("User ID", min_value=1, step=1)
        name = st.text_input("Name")
        email = st.text_input("Email")
        age = st.number_input("Age", min_value=0, step=1)
        join_date = st.date_input("Join Date")

        if st.button("Add User"):
            name = name.strip()
            email = email.strip()

            if not name:
                st.error("Name is required.")
            elif not email:
                st.error("Email is required.")
            else:
                payload = {
                    "user_id": int(user_id),
                    "name": name,
                    "email": email,
                    "age": int(age),
                    "join_date": str(join_date)
                }

                try:
                    response = requests.post(
                        f"{API_BASE_URL}/users",
                        json=payload,
                        timeout=5
                    )

                    if response.status_code == 201:
                        st.success("User added successfully.")
                        st.rerun()
                    else:
                        try:
                            error_json = response.json()
                            st.error(error_json.get("error", "Failed to add user."))
                        except Exception:
                            st.error("Failed to add user.")
                except requests.exceptions.ConnectionError:
                    st.error("Could not connect to the Flask API. Make sure backend/app.py is running.")
                except Exception as e:
                    st.error(f"Error connecting to API: {e}")





with tab2:
    try:
        filter_user_id = st.session_state.get("filter_user_id", None)

        if filter_user_id:
            response = requests.get(
                f"{API_BASE_URL}/user-workouts",
                params={"user_id": filter_user_id},
                timeout=5
            )
        else:
            response = requests.get(
                f"{API_BASE_URL}/user-workouts",
                timeout=5
            )

        if response.status_code == 200:
            workouts = response.json()
            df = pd.DataFrame(workouts)

            if not df.empty:
                df = df[["name","workout_id","exercise_name","num_sets","reps","weight_used","time_spent"]]
                df = df.reset_index(drop=True)

            st.data_editor(
                df,
                use_container_width=True,
                hide_index=True
            )


        else:
            try:
                error_json = response.json()
                st.error(f"Failed to fetch users: {error_json.get('error', 'Unknown error')}")
            except Exception:
                st.error("Failed to fetch users.")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the Flask API. Make sure backend/app.py is running.")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")

    with st.expander("Filter By User"):
        filter_user_id = st.number_input("User ID", min_value=1, step=1, key="filter_user")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Apply Filter"):
                st.session_state.filter_user_id = filter_user_id
                st.rerun()

        with col2:
            if st.button("Clear Filter"):
                st.session_state.filter_user_id = None
                st.rerun()

    st.subheader("Add New Workout")

    with st.expander("Workout Form"):
        workout_id = st.number_input("Workout ID", min_value=1, step=1, key="new_workout_id")
        workout_date = st.date_input("Workout Date", key="new_workout_date")
        duration_minutes = st.number_input("Duration (minutes)", min_value=0, step=1, key="new_duration")
        user_id = st.number_input("User ID", min_value=1, step=1, key="new_workout_user_id")

        if st.button("Add Workout"):
            payload = {
                "workout_id": int(workout_id),
                "workout_date": str(workout_date),
                "duration_minutes": int(duration_minutes),
                "user_id": int(user_id)
            }

            try:
                response = requests.post(
                    f"{API_BASE_URL}/workouts",
                    json=payload,
                    timeout=5
                )

                if response.status_code == 201:
                    st.success("Workout added successfully.")
                    st.rerun()
                else:
                    st.error("Failed to add workout.")
            except Exception as e:
                st.error(f"Error connecting to API: {e}")

with tab3:
    st.subheader("Workout Statistics")

    try:
        response = requests.get(f"{API_BASE_URL}/workout_stats", timeout=5)

        if response.status_code == 200:
            workout_stats = response.json()
            df = pd.DataFrame(workout_stats)

            if not df.empty:
                df = df[["User_id", "Name", "Number_Of_Workouts", "Time_Spent_Working_Out"]]
                df = df.reset_index(drop=True)

            st.data_editor(
                df,
                use_container_width=True,
                hide_index=True
            )



        else:
            try:
                error_json = response.json()
                st.error(f"Failed to fetch users: {error_json.get('error', 'Unknown error')}")
            except Exception:
                st.error("Failed to fetch users.")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the Flask API. Make sure backend/app.py is running.")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")
with tab4:
    st.subheader("User Goals")

    try:
        response = requests.get(f"{API_BASE_URL}/user_goal_info", timeout=5)

        if response.status_code == 200:
            workout_stats = response.json()
            df = pd.DataFrame(workout_stats)

            if not df.empty:
                df = df[["name", "user_id", "metric_type", "current_value","target_value","goal_status"]]
                df = df.reset_index(drop=True)

            st.data_editor(
                df,
                use_container_width=True,
                hide_index=True
            )



        else:
            try:
                error_json = response.json()
                st.error(f"Failed to fetch users: {error_json.get('error', 'Unknown error')}")
            except Exception:
                st.error("Failed to fetch users.")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the Flask API. Make sure backend/app.py is running.")
    except Exception as e:
        st.error(f"Error connecting to API: {e}")

    with st.expander("Add New Goal"):
        goal_id = st.number_input("Goal ID", min_value=1, step=1, key="new_goal_id")
        user_id = st.number_input("User ID", min_value=1, step=1, key="new_goal_user_id")
        metric_type = st.text_input("Metric Type", key="new_metric_type")
        current_value = st.number_input("Current Value", step=0.01, format="%.2f", key="new_current_value")
        target_value = st.number_input("Target Value", step=0.01, format="%.2f", key="new_target_value")
        start_date = st.date_input("Start Date", key="new_goal_start_date")
        end_date = st.date_input("End Date", key="new_goal_end_date")

        if st.button("Add Goal"):
            metric_type = metric_type.strip()

            if not metric_type:
                st.error("Metric type is required.")
            elif end_date < start_date:
                st.error("End date cannot be before start date.")
            else:
                payload = {
                    "goal_id": int(goal_id),
                    "user_id": int(user_id),
                    "metric_type": metric_type,
                    "current_value": float(current_value),
                    "target_value": float(target_value),
                    "start_date": str(start_date),
                    "end_date": str(end_date)
                }

                try:
                    response = requests.post(
                        f"{API_BASE_URL}/goals",
                        json=payload,
                        timeout=5
                    )

                    if response.status_code == 201:
                        st.success("Goal added successfully.")
                        st.rerun()
                    else:
                        try:
                            error_json = response.json()
                            st.error(error_json.get("error", "Failed to add goal."))
                        except Exception:
                            st.error("Failed to add goal.")
                except requests.exceptions.ConnectionError:
                    st.error("Could not connect to the Flask API. Make sure backend/app.py is running.")
                except Exception as e:
                    st.error(f"Error connecting to API: {e}")