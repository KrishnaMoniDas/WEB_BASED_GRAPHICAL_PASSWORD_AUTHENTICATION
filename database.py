import os
from sqlalchemy import create_engine, text


#connecting to the database
db_conn_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_conn_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

#fetching the users in the database and their id as a python dictionary
def load_users_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT number, id FROM users"))
    users = []
  rows = result.fetchall()
  for row in rows:
        user_dict = {'number': row[0], 'id': row[1]}
        users.append(user_dict)
  return users



# with engine.connect() as conn: 
#   result = conn.execute(text("SELECT number, id FROM users"))  
#   users = []
#   rows = result.fetchall()
#   for row in rows:
#         user_dict = {'number': row[0], 'id': row[1]}
#         users.append(user_dict)
#   print(users)

#function to fetch user from the database as thier id as argument


def load_user_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT id FROM users WHERE number = :id"), {"id": id})
    row = result.fetchone()
    if row is not None:
      return {'id': row[0]}
    else:
      return None


#fetching about page list from the 
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


# with engine.connect() as conn: 
#     result = conn.execute(text("SELECT * FROM about"))  
#     about = result.all()
#     about_first = str(about[0])
#     about_string = ""
#     for i in range(len(about_first)):
#       if about_first[i] != '(' and about_first[i] != ')' and about_first[i] != ',':
#         about_string = about_string + about_first[i]
#     print(about_string)


def submit_to_db(email, selection):
  with engine.connect() as conn:
    query = text("INSERT INTO users (id, passwd) VALUES (:email, :selection)")
    conn.execute(query, {"email": email, "selection": selection})




def valid_login(email,selection):
  with engine.connect() as conn:
    result = conn.execute(text("select id, passwd from users"))
    users = dict(result.all())
    
    if email in users.keys():
      if users[email] == selection:
        return 1
    else:
      return 0