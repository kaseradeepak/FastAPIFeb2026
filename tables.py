from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData() # metadata object stores the schema/structure of the table.

# Users table.
# users -> id, name, email
users = Table(
    "users", # name of the table.
    metadata,
    Column("id", Integer, primary_key=True), #primary_key -> it makes nullable=False, unique=True &auto-increment
    Column("name", String(50), nullable=False), # name can have max 50 characters.
    Column("email", String, unique=True, nullable=False)
)

# Create a new table to store products.

def create_tables():
    metadata.create_all(engine)