from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, DATETIME

Base = declarative_base()


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(70))
    Age = Column(Integer)
    Class = Column(String(20))


class Subjects(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50))


class Marks(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Student_id = Column(Integer, ForeignKey("students.id"))
    Subject_id = Column(Integer, ForeignKey("subjects.id"))
    Mark = Column(Integer)
    Date = Column(DATETIME)
    
