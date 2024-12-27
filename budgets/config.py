from flask import Flask
import mysql.connector

app = Flask(__name__)

<<<<<<< HEAD

=======
>>>>>>> 7f3e84380004f890a1d60e972b7cf980a7c15224
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Krishna1919@"
DB_NAME = "db1"

app.secret_key = "your_secret_key"

def get_db_connection():
    """Establish and return a database connection."""
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
