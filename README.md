# Project Name
COP4710_FINAL_PROJECT

## Team Members
- Subrina Myers
- Jordy Martinez
- Maksim Kharutski
- John Borrego

## Tech Stack
- Frontend: Streamlit
- Backend: Python 
- Database: MySQL 

## Prerequisites
List what someone needs installed before running the project:
- Python 3.x
- Streamlit
- MySQL

## Setup Instructions

### 1. Clone the repo
git clone https://github.com/johnb2005/COP4710_Final_Project.git
cd COP4710_Final_Project

## 2. Set up environment variables
Create a .env file in the backend folder:
DB_HOST=your-rds-endpoint
DB_USER=your-username
DB_PASSWORD=your-password
DB_NAME=your-database
DB_PORT=3306

### 4. Run the app
python app.py

## Features
├──frontend/
│   └── UI.py
├── backend/
│   └── app.py
└── README.md

## Database
db_proof/
│   ├── schema.sql
│   ├── data.sql
│   ├── constraints_test.sql
│   ├── queries.sql
│   └── query_outputs.txt