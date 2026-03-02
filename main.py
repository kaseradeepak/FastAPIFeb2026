# pip3 install fastapi pydantic uvicorn
# uvicorn main:app --reload
from fastapi import FastAPI, HTTPException, Path, Query, Depends
from commons import db_operations
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

# Query Param : Key-Value param
# /students?student_id=ST001
# @app.get("/studentss")
# def get_student_with_id(student_id: str = Query(..., description="Student Id", example="ST009")):
#     data = load_students_data()

#     if student_id not in data:
#         raise HTTPException(status_code=404, detail="Student not found.")
    
#     return data[student_id]

# Get the student details sorted (asc/desc) based on the input provided by the user
# Client should be able sort the students based on age or problems_solved.
# /students?sort_by=age?sort_order=asc
@app.get("/sort")
def get_students_in_sorted_order(sort_by: str = Query(..., description="Sort students on the basis of their age or problems_sovled."), sort_order: str = Query('asc', description="Sorting order - asc or desc")):
    valid_sort_by_fields = ['age', 'problems_sovled']

    if sort_by not in valid_sort_by_fields: 
        # HTTP Status Code - 400 : Bad Request.
        raise HTTPException(status_code=400, detail="Sorting is only supported by age or problems_sovled.")

    if sort_order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Sorting Order can only asc or desc")
    
    students_data = load_students_data()

    order = False # Asc
    if sort_order == 'desc':
        order = True 

    # reverse = True => Desc order
    # reverse = False => Asc order
    sorted_students_data = sorted(students_data.values(), key= lambda k: k.get(sort_by, 0), reverse=order)

    return sorted_students_data

# If we write common functionality in a separate file and function ->  this imrpoves reusability or our code.
# sample_api functionality depends upon db_operations functionality.
# Dependency Injection
@app.get("/api")
def sample_api(x = Depends(db_operations)):
    return x