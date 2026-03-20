# pip3 install sqlalchemy
# This file (db.py) will help to connect with Database.
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./masai.db" # sqlite / mysql / postresql /.....

engine = create_engine(DATABASE_URL, echo=True)

# ORM - Object Relational Mapping
# class Student:
#     id:int
#     name: str
#     age: int
#     batch: str
#     psp: float