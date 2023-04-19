import os
from sqlalchemy import create_engine, text

db_conn_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_conn_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


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


def load_user_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT id FROM users WHERE number = :id"), {"id": id})
    row = result.fetchone()
    if row is not None:
      return {'id': row[0]}
    else:
      return None



