from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime

Base = declarative_base()


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(70))
    Age = Column(Integer)
    Class = Column(String(20))

    def __init__(self, Name, Age, Class):
        self.Name = Name
        self.Age = Age
        self.Class = Class


class Subjects(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50))

    def __init__(self, Name):
        self.Name = Name


class Marks(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Student_id = Column(Integer, ForeignKey("students.id"))
    Subject_id = Column(Integer, ForeignKey("subjects.id"))
    Mark = Column(Integer)
    Date = Column(DateTime)

    def __init__(self, Student_id, Subject_id, Mark):
        self.Student_id = Student_id
        self.Subject_id = Subject_id
        self.Mark = Mark
    
