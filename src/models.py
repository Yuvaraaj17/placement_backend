from sqlalchemy import Column, Integer, String
from database import Base

class Questions(Base):
    __tablename__ = "questions"

    id=Column(Integer,primary_key=True,index=True)
    question_text=Column(String, index=True)
    choice_one=Column(String)
    choice_two=Column(String)
    choice_three=Column(String)
    choice_four=Column(String)
    correct_choice=Column(String)
    topic=Column(String)

class Users(Base):
    __tablename__ = "users"
    user_id=Column(Integer,primary_key=True)
    username=Column(String)
    password=Column(String)
    usertype=Column(String)


