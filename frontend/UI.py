import streamlit as st
import sys
import os
from datetime import date

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.connection import get_connection


# Initialize defaults
if "user_id" not in st.session_state:
    st.session_state.user_id = 1
if "name" not in st.session_state:
    st.session_state.name = ""
if "email" not in st.session_state:
    st.session_state.email = ""
if "age" not in st.session_state:
    st.session_state.age = 0
if "join_date" not in st.session_state:
    st.session_state.join_date = date.today()
if "reset_form" not in st.session_state:
    st.session_state.reset_form = False

# Reset BEFORE widgets are drawn
if st.session_state.reset_form:
    st.session_state.user_id = 1
    st.session_state.name = ""
    st.session_state.email = ""
    st.session_state.age = 0
    st.session_state.join_date = date.today()
    st.session_state.reset_form = False

st.title("PantherFitness Database")

tab1, = st.tabs(["Users"])

with tab1:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    st.dataframe(users)

    cursor.close()
    conn.close()

    st.number_input("User ID", min_value=1, step=1, key="user_id")
    st.text_input("Name", key="name")
    st.text_input("Email", key="email")
    st.number_input("Age", min_value=0, step=1, key="age")
    st.date_input("Join Date", key="join_date")

    if st.button("Add User"):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO Users (user_id, name, email, age, join_date)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (
                st.session_state.user_id,
                st.session_state.name,
                st.session_state.email,
                st.session_state.age,
                st.session_state.join_date
            )

            cursor.execute(query, values)
            conn.commit()

            st.session_state.reset_form = True
            st.success("User added successfully.")
            st.rerun()

        except Exception as e:
            st.error(f"Error adding user: {e}")

        finally:
            cursor.close()
            conn.close()