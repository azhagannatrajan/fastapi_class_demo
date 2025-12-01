from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import Base, SessionLocal, engine
import models
from pydantic import BaseModel

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# --------------------------
# FIXED DB CONNECTION
# --------------------------
def connect_db():
    db = SessionLocal()
    try:
        print("Connected to the DataBase")
        yield db
    finally:
        db.close()


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


@app.get("/marks")
def get_all_marks(dbs: Session = Depends(connect_db)):
    raw_query = "SELECT * FROM marks"
    result = dbs.execute(text(raw_query)).fetchall()
    return {"db_marks": [dict(row._mapping) for row in result]}


@app.get("/marks/{student_id}")
def get_marks_by_id(student_id: int):
    return {"message": f"Marks for ID = {student_id}"}

class StudentMarks(BaseModel):
    student_id: str
    student_name: str
    ps: int
    tech: int
    english: int
    lifeskills: int


@app.post("/marks")
def create_marks(new_marks: StudentMarks, db: Session = Depends(connect_db)):
    db_entry = models.Marks(
        student_id=new_marks.student_id,
        student_name=new_marks.student_name,
        ps=new_marks.ps,
        tech=new_marks.tech,
        english=new_marks.english,
        lifeskills=new_marks.lifeskills,
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return {
        "message": "Uploaded Marks Successfully",
        "data": {
            "student_id": db_entry.student_id,
            "name": db_entry.student_name,
            "ps": db_entry.ps,
            "tech": db_entry.tech,
            "english": db_entry.english,
            "ls": db_entry.lifeskills,
        },
    }


class UpdateStudentData(BaseModel):
    student_name: str
    ps: int
    tech: int
    english: int
    lifeskills: int


@app.put("/marks/{student_id}")
def update_marks(student_id: str, revised_marks: UpdateStudentData):
    for el in marks:
        if el["id"] == student_id:
            el["ps"] = revised_marks.ps
            el["tech"] = revised_marks.tech
            el["ls"] = revised_marks.lifeskills
            el["english"] = revised_marks.english
            el["name"] = revised_marks.student_name
            return {"message": "Successfully updated", "new_data": el}
    return {"message": "Student not found"}


@app.delete("/marks/{student_id}")
def delete_marks(student_id: str):
    for el in marks:
        if el["id"] == student_id:
            marks.remove(el)
            return {"message": "Deleted successfully"}
    return {"message": "Student not found"}


'''
---------------
   COACH
---------------
'''
@app.get("/")
def view(db:Session = Depends(connect_db)):
    pass
 


class Coach(BaseModel):
    coach_id :int
    coach_name:str
    email:str


@app.post("/coach")
def add_details(entry : Coach ,db:Session = Depends(connect_db)):
    db_entry = models.Coaches(
        coach_id = entry.coach_id,
        coach_name = entry.coach_name,
        email = entry.email
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)

class Update(BaseModel):
    name:str
    email:str

@app.put("/coach")
def update_details(id :int,update:Update,db: Session = Depends(connect_db)):
    db_update = db.query(models.Coaches).filter(models.Coaches.coach_id == id).first()
    if db_update:
        db_update.coach_name = update.name
        db_update.email = update.email
        db.commit()
    return "updated successfully"
    


@app.delete("/coach/delete")
def delete(id : int,db:Session= Depends(connect_db)):
     db_delete = db.query(models.Coaches).filter(models.Coaches.coach_id == id).first()
     if db_delete:
        db.delete(db_delete)
        db.commit()
     return " deleted successfully"