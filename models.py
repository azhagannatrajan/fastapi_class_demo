from sqlalchemy import Column, String, Integer
from database import Base

class Marks(Base):
    __tablename__ = "marks"

    student_id = Column(String, primary_key=True)
    student_name = Column(String)
    ps = Column(Integer)
    english = Column(Integer)
    tech = Column(Integer)
    lifeskills = Column(Integer)