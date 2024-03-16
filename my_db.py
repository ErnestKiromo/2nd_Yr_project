import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8181@8181ek',
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the database creation query
create_database = """
CREATE DATABASE IF NOT EXISTS dbpython;
"""

# Execute the database creation query
cursor.execute(create_database)

# Commit changes and close cursor
conn.commit()
cursor.close()

# Connect to the MySQL server
conn = mysql.connector.connect(
    host='localhost',
    database='dbpython',
    user='root',
    password='8181@8181ek',
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define SQL queries to create tables
create_users = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NULL,
    email VARCHAR(255) NULL,
    password VARCHAR(255) NULL,
    token VARCHAR(255) NULL,
    active_or_blocked VARCHAR(255) NULL,
    phone VARCHAR(20) NULL,
    last_login TIMESTAMP NULL
)
"""

create_dashboard = """
CREATE TABLE IF NOT EXISTS dashboard (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image VARCHAR(255) NULL,
    likes INT NULL,
    price INT NULL,
    title VARCHAR(255) NULL,
    type VARCHAR(255) NULL,
    description VARCHAR(255) NULL,
    location VARCHAR(20) NULL,
    seller_id INT NULL,
    reported INT NULL,
    whatsapp_visits INT NULL
)
"""

create_blog = """
CREATE TABLE IF NOT EXISTS blog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    color VARCHAR(255) NULL,
    title VARCHAR(255) NULL,
    subtitle VARCHAR(255) NULL,
    type VARCHAR(255) NULL,
    blog VARCHAR(255) NULL,
    likes INT NULL,
    forwards INT NULL,
    seller_id INT NULL,
    category INT NULL
)
"""

create_memories_and_happenings = """
CREATE TABLE IF NOT EXISTS memories_and_happenings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image VARCHAR(255) NULL,
    text VARCHAR(255) NULL,
    type VARCHAR(255) NULL,
    likes INT NULL,
    dislikes INT NULL,
    seller_id INT NULL
)
"""

create_house_to_rent = """
CREATE TABLE IF NOT EXISTS house_to_rent (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image VARCHAR(255) NULL,
    price INT NULL,
    description VARCHAR(255) NULL,
    name VARCHAR(255) NULL,
    type VARCHAR(255) NULL,
    seller_id INT NULL
)
"""

create_educational_materials = """
CREATE TABLE IF NOT EXISTS educational_materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    color VARCHAR(255) NULL,
    title VARCHAR(255) NULL,
    subtitle VARCHAR(255) NULL,
    type VARCHAR(255) NULL,
    blog VARCHAR(255) NULL,
    likes INT NULL,
    forwards INT NULL,
    seller_id INT NULL,
    category INT NULL
)
"""

create_entertainment = """
CREATE TABLE IF NOT EXISTS entertainment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    color VARCHAR(255) NULL,
    title VARCHAR(255) NULL,
    type VARCHAR(255) NULL,
    description VARCHAR(255) NULL,
    link VARCHAR(255) NULL,
    likes INT NULL,
    seller_id INT NULL,
    image VARCHAR(255) NULL,
    video VARCHAR(255) NULL
)
"""

create_ads = """
CREATE TABLE IF NOT EXISTS ads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    color VARCHAR(255) NULL,
    title VARCHAR(255) NULL,
    link VARCHAR(255) NULL,
    clicks INT NULL,
    seller_id INT NULL,
    image VARCHAR(255) NULL
)
"""
# Execute the SQL queries to create tables
cursor.execute(create_users)
cursor.execute(create_dashboard)
cursor.execute(create_blog)
cursor.execute(create_memories_and_happenings)
cursor.execute(create_house_to_rent)
cursor.execute(create_educational_materials)
cursor.execute(create_entertainment)
cursor.execute(create_ads)

# Commit changes and close connection
conn.commit()
conn.close()

print("Tables created successfully!")
