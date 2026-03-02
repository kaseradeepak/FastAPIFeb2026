# pip3 install sqlalchemy
# This file (db.py) will help to connect with Database.
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./masai.db"

engine = create_engine(DATABASE_URL, echo=True)