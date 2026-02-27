# pip3 install fastapi pydantic uvicorn
# uvicorn main:app --reload
from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

# localhost:8000/hello
@app.get("/hello")
def say_hello():
    return "Hello Everyone!"

# localhost:8000/bye
@app.get("/bye")
def say_bye():
    return "Bye Everyone!"

def load_students_data():
    # Load students data from students.json file.
    with open('students.json', 'r') as f:
        students_data = json.load(f)

    return students_data

# Get all the students.
# /students
@app.get("/students")
def get_all_students():
    # return alll the students from students.json file.
    return load_students_data()

# /students/ST001
# Path Params  => passed via curly braces.
# Three dots inside Path function => Mandatory param.
@app.get("/students/{student_id}")
def get_student_with_id(student_id: str = Path(..., description="Id of the student which you want to access.", example="ST007")):
    data = load_students_data()

    if student_id not in data:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    return data[student_id]

# Query Param
# /students?student_i=ST001
# @app.get("/studentss")
# def get_student_with_id(student_id: str = Query(..., description="Student Id", example="ST009")):
#     data = load_students_data()

#     if student_id not in data:
#         raise HTTPException(status_code=404, detail="Student not found.")
    
#     return data[student_id]

# Get the student details sorted (asc/desc) based on the input provided by the user
# /students?sort_by=""?sort_order="asc/desc"