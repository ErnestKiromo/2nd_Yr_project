from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
import mysql.connector
from typing import List

# app = FastAPI()
app = FastAPI(debug=True)

# Configure CORS to allow frontend from another url to pass data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5501"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

host = 'localhost'
database = 'dbpython'
user = 'root'
password = '8181@8181ek'

# Establishing a connection to the MySQL database
connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

# Dependency to get a database cursor
def get_db_cursor():
    try:
        if connection.is_connected():
            print('Connected to MySQL database')
            # Create a cursor to execute SQL queries
            cursor = connection.cursor(dictionary=True)
            # Execute query to create database session
            yield cursor
        else:
            print('Connection failed')

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
        raise HTTPException(status_code=500, detail="Database connection error")

    finally:
        print("Closing connection")
        # Close the connection when done
        if 'connection' in locals():
            connection.close()

class UserSignup(BaseModel):
    username: str
    email: str
    password: str

@app.post("/signup")
async def signup(user_data: UserSignup, db_cursor: dict = Depends(get_db_cursor)):
    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    values = (user_data.username, user_data.email, user_data.password)
    try:
        db_cursor.execute(query, values)
        # db_cursor.connection.commit()  # Commit the transaction
        connection.commit()
        return {"message": "User signed up successfully"}
    except mysql.connector.Error as e:
        print("Database error:", e)
        db_cursor.connection.rollback()  # Rollback the transaction in case of an error
        raise HTTPException(status_code=500, detail="Database error occurred")
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
    finally:
        # Close the cursor after executing the query
        db_cursor.close()


# Define a response model for user data
class UserData(BaseModel):
    id: int
    username: str
    email: str
    active_blocked: str
    selling_buying: str
    online_offline: str

# Endpoint to get user data by ID
@app.get("/users/{user_id}", response_model=UserData)
async def get_user(user_id: int, db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve user data by ID
    query = "SELECT id, username, email, active_blocked, selling_buying, online_offline FROM users WHERE id = %s"
    db_cursor.execute(query, (user_id,))
    user_data = db_cursor.fetchone()

    # Check if user data exists
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    return user_data

# Endpoint to get all users data
@app.get("/all-users", response_model=List[UserData])
async def get_all_users(db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve all user data
    query = "SELECT id, username, email, active_blocked, selling_buying, online_offline FROM users"
    db_cursor.execute(query)
    users_data = db_cursor.fetchall()

    # Check if any user data exists
    if not users_data:
        raise HTTPException(status_code=404, detail="No users found")

    return users_data



