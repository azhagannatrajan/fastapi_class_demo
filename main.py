from fastapi import FastAPI
# step 1
from pydantic import BaseModel

app = FastAPI()

@app.get("/test")
def welcome_kit():
    print("hello world")
    return {"message": "Welcome to our server"}
marks = [
    {
        "name": "narayanan",
        "id": "1",
        "ps": 72,
        "tech": 35,
        "english": 40,
        "ls": 38,
    },
    {
        "name": "kamalesh",
        "id": "2",
        "ps": 73,
        "tech": 34,
        "english": 20,
        "ls": 78,
    },
]
# get all marks
@app.get("/marks")
def get_all_marks():
    if len(marks) == 0:
        return {"message": "This end point will return all the marks"}
    else:
        # return {"marks": marks}
        return marks
    
# get marks by id
@app.get("/marks/{student_id}")
def get_marks_by_id(student_id: int):
    return {
        "message": f"This end point will return marks for student no - {student_id}"
    }

# step 2
# create a class for the student marks
class StudentMarks(BaseModel):
    student_id: str
    student_name: str
    ps: int
    tech: int
    english: int
    lifeskills: int

# create marks
@app.post("/marks")
def create_marks(new_marks: StudentMarks):
    # extract separate data
    my_name = new_marks.student_name
    ps_mark = new_marks.ps
    tech_mark = new_marks.tech
    english = new_marks.english
    ls = new_marks.lifeskills
    my_id = new_marks.student_id
    # packing into a dictionary
    info = {}
    info.update(
        {
            "name": my_name,
            "id": my_id,
            "ps": ps_mark,
            "tech": tech_mark,
            "english": english,
            "ls": ls,
        }
    )
    marks.append(info)
    return {"message": "Uploaded Marks Successfully"}
class UpdateStudentData(BaseModel):
    student_name: str
    ps: int
    tech: int
    english: int
    lifeskills: int

# student_id is called Request Params
# revised_marks is called Request Body (or) Payload

@app.put("/marks/{student_id}")
def update_marks(student_id: str, revised_marks: UpdateStudentData):
    for el in marks:
        # id is compared here
        if el["id"] == student_id:
            # i dont know which mark is getting updated
            el["ps"] = revised_marks.ps
            el["tech"] = revised_marks.tech
            el["ls"] = revised_marks.lifeskills
            el["english"] = revised_marks.english
            el["name"] = revised_marks.student_name
    return {"message": "testing phase"}
@app.delete("/marks/{student_id}")
def delete_marks(student_id:str):
    # write your code logic here
    pass