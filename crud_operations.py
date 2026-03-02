from db import engine
from tables import users
from sqlalchemy import insert

# Create User
def create_user(input_name: str, input_email: str):
    with engine.connect() as conn:
        # insert into users values('Abhishek', 'abhishek@google.com')
        query = insert(users).values(name=input_name, email=input_email)
        conn.execute(query)
        conn.commit()


