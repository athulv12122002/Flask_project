import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("user_data.db")
cursor = connection.cursor()

# Create the table with the correct column names
command = """CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
)"""

cursor.execute(command)

# Insert sample data
cursor.execute("INSERT INTO users (name, email, password) VALUES ('Athul', 'athul@example.com', '12345')")
cursor.execute("INSERT INTO users (name, email, password) VALUES ('Kiran', 'kiran@example.com', '54321')")
cursor.execute("INSERT INTO users (name, email, password) VALUES ('Dileep', 'dileep@example.com', '67890')")

# Commit changes and close the connection
connection.commit()
connection.close()
