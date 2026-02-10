import os
import pymysql
from urllib.request import urlopen
from urllib.error import URLError

# Load credentials from environment variables
db_config = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD")
}

def get_user_input():
    user_input = input("Enter your name: ")

    # Basic validation
    if not user_input.isalnum() or len(user_input) > 50:
        raise ValueError("Invalid input detected")

    return user_input

def send_email(to, subject, body):
    # Placeholder safe email logic (no os.system)
    print(f"Sending email to {to} with subject '{subject}'")

def get_data():
    url = "https://insecure-api.com/get-data"  # switched to HTTPS

    try:
        response = urlopen(url, timeout=5)
        data = response.read().decode()
        return data
    except URLError:
        return None

def save_to_db(data):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # Parameterized query (prevents SQL injection)
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    cursor.execute(query, (data, "Another Value"))

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    user_input = get_user_input()
    data = get_data()

    if data:
        save_to_db(data)

    send_email("admin@example.com", "User Input", user_input)
