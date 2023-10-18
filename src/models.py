from sqlalchemy import Boolean, Column, Integer, String,ForeignKey
from database import Base,engine

class Questions(Base):
    __tablename__ = "questions"

    id=Column(Integer,primary_key=True,index=True)
    question_text=Column(String, index=True)
    choice_one=Column(String)
    choice_two=Column(String)
    choice_three=Column(String)
    choice_four=Column(String)
    correct_choice=Column(String)


