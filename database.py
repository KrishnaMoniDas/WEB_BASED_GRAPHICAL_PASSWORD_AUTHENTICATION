import os
from sqlalchemy import create_engine, text

db_conn_string = os.environ['DB_CONNECTION_STRING']

engine=create_engine(db_conn_string,
                    connect_args={
                      "ssl":{
                        "ssl_ca" : "/etc/ssl/cert.pem"
                      }
                    }
                    )

def load_users_from_db():
  with engine.connect() as conn :
    result = conn.execute(text("select * from users"))
    users = []
    for row in result:
      user_dict = {column[0]:value for column, value in zip(result.cursor.description, row)}
      users.append(user_dict)
      
    return users



with engine.connect() as conn :
    result = conn.execute(text("select * from users"))
    users = []
    for row in result:
      user_dict = {column[0]:value for column, value in zip(result.cursor.description, row)}
      users.append(user_dict)
      
    print(users)

