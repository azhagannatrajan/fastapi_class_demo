from pydantic import BaseModel

class StudentsData(BaseModel):
    student_name: str
    ps: int
    tech: int
    english: int
    lifeskills: inta