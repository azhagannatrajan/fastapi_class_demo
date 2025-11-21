from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

# create a class for the student marks
class StudentMarks(BaseModel):
    student_id: str
    ps: int
    tech: int
    english: int
    life_skills: int


# @ = annotations,decorator
@app.get("/test")
def greet():
    return {"hello": "world!"}


# get all marks
@app.get("/marks")
def get_marks():
    return {"message":"This end point will return all the marks"}

# get mark by id
@app.get("/marks/{student_id}")
def get_marks_by_id(student_id):
    print(student_id)
    return {"message": f"This end point will return the marks with student no.{student_id}"}

# create marks 
@app.post("/marks")
def create_marks(new_marks: StudentMarks):
    print(new_marks)
    pass