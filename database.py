import os
from sqlalchemy import create_engine, text
from misc import algorithm_implementation
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Supabase DB connection string using environment variables
db_conn_string = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Create an engine with the Supabase PostgreSQL connection string
engine = create_engine(db_conn_string, connect_args={"sslmode": "require"})

# Fetching the users in the database and their id as a Python dictionary
def load_users_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT number, id FROM users"))
        users = []
        rows = result.fetchall()
        for row in rows:
            user_dict = {'number': row[0], 'id': row[1]}
            users.append(user_dict)
    return users

# Fetch user from the database using their id as argument
def load_user_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id FROM users WHERE number = :id"), {"id": id})
        row = result.fetchone()
        if row is not None:
            return {'id': row[0]}
        else:
            return None

# Fetch about page list from the database
def about_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM about"))
        about = result.all()
        about_first = str(about[0])
        about_string = ""
        for i in range(len(about_first)):
            if about_first[i] != '(' and about_first[i] != ')' and about_first[i] != ',':
                about_string = about_string + about_first[i]
        return about_string

# Insert new user into the database
def submit_to_db(email, selection):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT number FROM users"))
        users = {row[0] for row in result.fetchall()}  # Set for faster lookup

        if email in users:
            return 0  # User already exists
        else:
            query = text("INSERT INTO users (number, passwd) VALUES (:email, :selection)")
            selection = algorithm_implementation(selection)

            try:
                conn.execute(query, {"email": email, "selection": selection})
                conn.commit()  # Commit the transaction
                return 1  # Success
            except Exception as e:
                print("Error inserting user:", e)
                return 0  # Failure

# Validate user login
def valid_login(email, selection):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT number, passwd FROM users"))
        users = dict(result.all())
        selection = algorithm_implementation(selection)
        if email in users.keys():
            if users[email] == selection:
                return 1
        else:
            return 0
