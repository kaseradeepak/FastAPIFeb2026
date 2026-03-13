from db import engine
from tables import users
from sqlalchemy import insert, select, update, delete

# CRUD - Create, Reads, Update & Delete

# Create User
def create_user(input_name: str, input_email: str):
    with engine.connect() as conn:
        # insert into users values('Abhishek', 'abhishek@google.com')
        query = insert(users).values(name=input_name, email=input_email)
        conn.execute(query)
        conn.commit()

# Read
def get_user_by_id(input_user_id: int):
    with engine.connect() as conn:
        # select * from users where id = 1234
        query = select(users).where(users.c.id == input_user_id)
        data = conn.execute(query).first()
        return data

def get_all_users():
    with engine.connect() as conn:
        query = select(users)
        data = conn.execute(query).fetchall()
        return data

# Update
def update_user_name(input_user_id: int, input_user_name: str):
    with engine.connect() as conn:
        # update users set name = new_name where id = input_user_id
        query = update(users).where(users.c.id == input_user_id).values(name = input_user_name)
        conn.execute(query)
        conn.commit()

# Delete
def delete_user_by_id(input_user_id: int):
    with engine.connect() as conn:
        query = delete(users).where(users.c.id == input_user_id)
        conn.execute(query)
        conn.commit()
