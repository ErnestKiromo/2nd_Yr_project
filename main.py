import datetime
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
import mysql.connector
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
import mysql.connector.errors
from typing import Any

# app = FastAPI()
app = FastAPI(debug=True)

# Configure CORS settings
origins = [
    "http://127.0.0.1:5501/sell.html",
    "http://127.0.0.1:5501",
]

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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
    name: str
    email: str
    password: str

@app.post("/signup")
async def signup(user_data: UserSignup, db_cursor: dict = Depends(get_db_cursor)):
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    values = (user_data.name, user_data.email, user_data.password)
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
    name: Any
    email: Any
    active_or_blocked: Any
    phone: Any
    # last_login: Union[str, datetime.datetime]

# Endpoint to get user data by ID
@app.get("/users/{user_id}", response_model=UserData)
async def get_user(user_id: int, db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve user data by ID
    query = "SELECT id, name, email, active_or_blocked, phone, last_login FROM users WHERE id = %s"
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
    query = "SELECT id, name, email, active_or_blocked, phone, last_login FROM users"
    db_cursor.execute(query)
    users_data = db_cursor.fetchall()

    # Check if any user data exists
    if not users_data:
        raise HTTPException(status_code=404, detail="No users found")

    return users_data
# end sighup

# Dashboard
# Define a response model for Product data
class Product(BaseModel):
    # id: int
    image: str
    likes: int
    price: int
    title: str
    category: str
    description: str
    location: str
    seller_id: int
    reported: int
    whatsapp_visits: int

# product upload
@app.post("/product")
async def signup(user_data: Product, db_cursor: dict = Depends(get_db_cursor)):
    print(user_data)
    query = "INSERT INTO dashboard (image, likes, price, title, category, description, location, seller_id, reported, whatsapp_visits) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (user_data.image, 0, user_data.price, user_data.title, user_data.category, user_data.description, user_data.location, user_data.seller_id, user_data.reported, user_data.whatsapp_visits)
    try:
        db_cursor.execute(query, values)
        # db_cursor.connection.commit()  # Commit the transaction
        connection.commit()
        return {"message": "Product uploaded successfully."}
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

class Product2(BaseModel):
    id: int
    image: str
    likes: int
    price: int
    title: str
    category: str
    description: str
    location: str
    seller_id: int
    reported: int
    whatsapp_visits: int

# Endpoint to get user data by ID
@app.get("/product/{user_id}", response_model=Product2)
async def get_user(user_id: int, db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve user data by ID
    query = "SELECT id, image, likes, price, title, category, description, location, seller_id, reported, whatsapp_visits FROM dashboard WHERE id = %s"
    db_cursor.execute(query, (user_id,))
    user_data = db_cursor.fetchone()

    # Check if user data exists
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    return user_data


# Endpoint to get all users data
@app.get("/all-products", response_model=List[Product2])
async def get_all_products(db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve all user data
    query = "SELECT id, image, likes, price, title, category, description, location, seller_id, reported, whatsapp_visits FROM dashboard"
    db_cursor.execute(query)
    product_data = db_cursor.fetchall()

    # Check if any user data exists
    if not product_data:
        raise HTTPException(status_code=404, detail="No product found")

    return product_data
# end product

# Blogs
class Blogs(BaseModel):
    # id: int
    color: str
    title: str
    subtitle: str
    category: str
    blog: str
    likes: int
    forwards: int
    seller_id: int


@app.post("/Blogs")
async def Blogz(user_data: Blogs, db_cursor: dict = Depends(get_db_cursor)):
    print(user_data)
    query = "INSERT INTO blog (color,title, subtitle, category, blog, likes, forwards, seller_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (user_data.color, user_data.title, user_data.subtitle, user_data.category, user_data.blog, user_data.likes, user_data.forwards, user_data.seller_id)
    try:
        db_cursor.execute(query, values)
        connection.commit()
        return {"message": "Blogs uploaded successfully."}
    except mysql.connector.Error as e:
        print("Database error:", e)
        connection.rollback()  # Rollback the transaction using the connection object
        raise HTTPException(status_code=500, detail="Database error occurred")
    except mysql.connector.errors.ProgrammingError as e:
        print("Programming error:", e)
        connection.rollback()  # Rollback the transaction using the connection object
        raise HTTPException(status_code=500, detail="Programming error occurred")
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
    finally:
        db_cursor.close()  

class blog2(BaseModel):
    id: int
    color: Any
    title: Any
    subtitle: Any
    category: Any
    blog: Any
    likes: Any
    forwards: Any
    seller_id: Any

# Endpoint to get blog data by ID
@app.get("/blog/{blog_id}", response_model=blog2)
async def get_blog(blog_id: int, db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve blog data by ID
    query = "SELECT id, color, title, subtitle, category, blog, likes, forwards, seller_id FROM blog WHERE id = %s"
    db_cursor.execute(query, (blog_id,))
    blog_data = db_cursor.fetchone()

    # Check if blog data exists
    if not blog_data:
        raise HTTPException(status_code=404, detail="Blog not found")

    # Convert fetched data into a blog2 model instance
    return blog2(**blog_data)


# Endpoint to get all blogs data
@app.get("/all-blogs", response_model=List[blog2])
async def get_all_blogs(db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve all user data
    query = "SELECT id, color, title, subtitle, category, blog, likes, forwards, seller_id FROM blog"
    db_cursor.execute(query)
    product_data = db_cursor.fetchall()

    # Check if any user data exists
    if not product_data:
        raise HTTPException(status_code=404, detail="No product found")

    return product_data
# end blog


# Ads
class Ads(BaseModel):
    # id: int
    color: str
    title: str
    link: str
    seller_id: int
    clicks: int


@app.post("/Ads")
async def Adz(user_data: Ads, db_cursor: dict = Depends(get_db_cursor)):
    print(user_data)
    query = "INSERT INTO ads (color,title, link, seller_id, clicks) VALUES (%s, %s, %s, %s, %s)"
    values = (user_data.color, user_data.title, user_data.link, user_data.seller_id, user_data.clicks)
    try:
        db_cursor.execute(query, values)
        connection.commit()
        return {"message": "Ads uploaded successfully."}
    except mysql.connector.Error as e:
        print("Database error:", e)
        connection.rollback()  # Rollback the transaction using the connection object
        raise HTTPException(status_code=500, detail="Database error occurred")
    except mysql.connector.errors.ProgrammingError as e:
        print("Programming error:", e)
        connection.rollback()  # Rollback the transaction using the connection object
        raise HTTPException(status_code=500, detail="Programming error occurred")
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
    finally:
        db_cursor.close()  

class Ads2(BaseModel):
    id: int
    color: Any
    title: Any
    link: Any
    seller_id: Any
    clicks: Any
    image: Any


# Endpoint to get ads data by ID
@app.get("/ads/{Ad_id}", response_model=Ads2)
async def get_blog(Ad_id: int, db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve blog data by ID
    query = "SELECT id, color, title, link, seller_id, clicks FROM ads WHERE id = %s"
    db_cursor.execute(query, (Ad_id,))
    blog_data = db_cursor.fetchone()

    # Check if blog data exists
    if not blog_data:
        raise HTTPException(status_code=404, detail="Ad not found")

    # Convert fetched data into a blog2 model instance
    return Ads2(**blog_data)


# Endpoint to get all ads data
@app.get("/all-ads", response_model=List[Ads2])
async def get_all_blogs(db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve all user data
    query = "SELECT id, color, title, link, seller_id, image, clicks FROM ads"
    db_cursor.execute(query)
    product_data = db_cursor.fetchall()

    # Check if any user data exists
    if not product_data:
        raise HTTPException(status_code=404, detail="No product found")

    return product_data
# end ads

# Memories and happenings
class Memoriez(BaseModel):
    # id: int
    likes: int
    text: str
    category: str
    seller_id: int
    dislikes: int


@app.post("/Memories")
async def Memories(user_data: Memoriez, db_cursor: dict = Depends(get_db_cursor)):
    print(user_data)
    query = "INSERT INTO memories_and_happenings (likes,text, category, seller_id, dislikes) VALUES (%s, %s, %s, %s, %s)"
    values = (user_data.likes, user_data.text, user_data.category, user_data.seller_id, user_data.dislikes)
    try:
        db_cursor.execute(query, values)
        connection.commit()
        return {"message": "Memories uploaded successfully."}
    except mysql.connector.Error as e:
        print("Database error:", e)
        connection.rollback()  # Rollback the transaction using the connection object
        raise HTTPException(status_code=500, detail="Database error occurred")
    except mysql.connector.errors.ProgrammingError as e:
        print("Programming error:", e)
        connection.rollback()  # Rollback the transaction using the connection object
        raise HTTPException(status_code=500, detail="Programming error occurred")
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
    finally:
        db_cursor.close()  

class Memories2(BaseModel):
    id: int
    likes: Any
    text: Any
    category: Any
    seller_id: Any
    dislikes: Any
    image: Any


# Endpoint to get memories_and_happenings data by ID
@app.get("/memorie/{Memorie_id}", response_model=Memories2)
async def get_Memories(Memorie_id: int, db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve blog data by ID
    query = "SELECT id, likes,text, category, seller_id, image, dislikes FROM memories_and_happenings WHERE id = %s"
    db_cursor.execute(query, (Memorie_id,))
    blog_data = db_cursor.fetchone()

    # Check if blog data exists
    if not blog_data:
        raise HTTPException(status_code=404, detail="Memorie not found")

    # Convert fetched data into a blog2 model instance
    return Memories2(**blog_data)


# Endpoint to get all memories_and_happenings data
@app.get("/all-Memories", response_model=List[Memories2])
async def get_all_memories(db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve all user data
    query = "SELECT id, likes,text, category, image, seller_id, dislikes FROM memories_and_happenings"
    db_cursor.execute(query)
    product_data = db_cursor.fetchall()

    # Check if any user data exists
    if not product_data:
        raise HTTPException(status_code=404, detail="No Memories found")

    return product_data
# end memories_and_happenings

# Accomodation
class Accomodation(BaseModel):
    # id: int
    price: int
    category: str
    description: str
    seller_id: int
    vacant: str
    name: str

@app.post("/Housetorent")
async def Housetorent(user_data: Accomodation, db_cursor: dict = Depends(get_db_cursor)):
    print(user_data)
    query = "INSERT INTO house_to_rent (price,category, description, seller_id, vacant, name) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (user_data.price, user_data.category, user_data.description, user_data.seller_id, user_data.vacant, user_data.name)
    try:
        db_cursor.execute(query, values)
        connection.commit()
        return {"message": "Accomodation uploaded successfully."}
    except mysql.connector.Error as e:
        print("Database error:", e)
        connection.rollback()  # Rollback the transaction using the connection object
        raise HTTPException(status_code=500, detail="Database error occurred")
    except mysql.connector.errors.ProgrammingError as e:
        print("Programming error:", e)
        connection.rollback()  # Rollback the transaction using the connection object
        raise HTTPException(status_code=500, detail="Programming error occurred")
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
    finally:
        db_cursor.close()  

class Accomodation2(BaseModel):
    id: int
    price: Any
    category: Any
    description: Any
    seller_id: Any
    vacant: Any
    name: Any
    image: Any


# Endpoint to get memories_and_happenings data by ID
@app.get("/Accomodation/{Accomodation_id}", response_model=Accomodation2)
async def get_Memories(Accomodation_id: int, db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve blog data by ID
    query = "SELECT id, price,category, description, image, seller_id, vacant, name FROM house_to_rent WHERE id = %s"
    db_cursor.execute(query, (Accomodation_id,))
    blog_data = db_cursor.fetchone()

    # Check if blog data exists
    if not blog_data:
        raise HTTPException(status_code=404, detail="Accomodation not found")

    # Convert fetched data into a blog2 model instance
    return Accomodation2(**blog_data)


# Endpoint to get all memories_and_happenings data
@app.get("/all-Accomodation", response_model=List[Accomodation2])
async def get_all_memories(db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve all user data
    query = "SELECT id, price,category, description, image, seller_id, vacant, name FROM house_to_rent"
    db_cursor.execute(query)
    product_data = db_cursor.fetchall()

    # Check if any user data exists
    if not product_data:
        raise HTTPException(status_code=404, detail="No Accomodation found")

    return product_data
# end memories_and_happenings

# Entertainment
class Entertainment(BaseModel):
    # id: int
    likes: int
    title: str
    category: str
    description: str
    seller_id: int
    color: str
    link: str

@app.post("/podcast")
async def entertainment(user_data: Entertainment, db_cursor: dict = Depends(get_db_cursor)):
    print(user_data)
    query = "INSERT INTO entertainment (likes,link, title, category, description, seller_id, color) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (user_data.likes, user_data.link, user_data.title, user_data.category, user_data.description, user_data.seller_id, user_data.color)
    try:
        db_cursor.execute(query, values)
        connection.commit()
        return {"message": "Entertainment uploaded successfully."}
    except mysql.connector.Error as e:
        print("Database error:", e)
        connection.rollback()  # Rollback the transaction using the connection object
        raise HTTPException(status_code=500, detail="Database error occurred")
    except mysql.connector.errors.ProgrammingError as e:
        print("Programming error:", e)
        connection.rollback()  # Rollback the transaction using the connection object
        raise HTTPException(status_code=500, detail="Programming error occurred")
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
    finally:
        db_cursor.close()  

class Entertainment2(BaseModel):
    id: int
    likes: Any
    title: Any
    category: Any
    description: Any
    seller_id: Any
    color: Any
    link: Any


# Endpoint to get memories_and_happenings data by ID
@app.get("/entertainment/{entertainment_id}", response_model=Entertainment2)
async def get_entertainment(entertainment_id: int, db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve blog data by ID
    query = "SELECT id, likes,link, title, category, description, seller_id, color FROM entertainment WHERE id = %s"
    db_cursor.execute(query, (entertainment_id,))
    blog_data = db_cursor.fetchone()

    # Check if blog data exists
    if not blog_data:
        raise HTTPException(status_code=404, detail="Entertainment not found")

    # Convert fetched data into a blog2 model instance
    return Entertainment2(**blog_data)


# Endpoint to get all memories_and_happenings data
@app.get("/all-Entertainment", response_model=List[Entertainment2])
async def get_all_entertainment(db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve all user data
    query = "SELECT id, likes,link, title, category, description, seller_id, color FROM entertainment"
    db_cursor.execute(query)
    product_data = db_cursor.fetchall()

    # Check if any user data exists
    if not product_data:
        raise HTTPException(status_code=404, detail="No entertainment found")

    return product_data
# end entertainment

# Education
class Education(BaseModel):
    # id: int
    likes: int
    title: str
    subtitle: str
    category: str
    blog: str
    seller_id: int
    forwards: int
    color: str

@app.post("/uploadEducation")
async def education(user_data: Education, db_cursor: dict = Depends(get_db_cursor)):
    print(user_data)
    query = "INSERT INTO educational_materials (likes, title, subtitle, category, blog, seller_id, forwards, color) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (user_data.likes, user_data.title, user_data.subtitle, user_data.category, user_data.blog, user_data.seller_id, user_data.forwards, user_data.color)
    try:
        db_cursor.execute(query, values)
        connection.commit()
        return {"message": "Education uploaded successfully."}
    except mysql.connector.Error as e:
        print("Database error:", e)
        connection.rollback()  # Rollback the transaction using the connection object
        raise HTTPException(status_code=500, detail="Database error occurred")
    except mysql.connector.errors.ProgrammingError as e:
        print("Programming error:", e)
        connection.rollback()  # Rollback the transaction using the connection object
        raise HTTPException(status_code=500, detail="Programming error occurred")
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
    finally:
        db_cursor.close()  


class Education2(BaseModel):
    id: int
    likes: Any
    title: Any
    subtitle: Any
    category: Any
    blog: Any
    seller_id: Any
    forwards: Any
    color: Any


# Endpoint to get education data by ID
@app.get("/education/{education_id}", response_model=Education2)
async def get_education(education_id: int, db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve blog data by ID
    query = "SELECT id, likes, title, subtitle, category, blog, seller_id, forwards, color FROM educational_materials WHERE id = %s"
    db_cursor.execute(query, (education_id,))
    blog_data = db_cursor.fetchone()

    # Check if blog data exists
    if not blog_data:
        raise HTTPException(status_code=404, detail="Education not found")

    # Convert fetched data into a blog2 model instance
    return Education2(**blog_data)


# Endpoint to get all Education data
@app.get("/all-education", response_model=List[Education2])
async def get_all_education(db_cursor: dict = Depends(get_db_cursor)):
    # Execute query to retrieve all user data
    query = "SELECT id, likes, title, subtitle, category, blog, seller_id, forwards, color FROM educational_materials"
    db_cursor.execute(query)
    product_data = db_cursor.fetchall()

    # Check if any user data exists
    if not product_data:
        raise HTTPException(status_code=404, detail="No Education found")

    return product_data
# end educational_materials