from typing import List, Annotated
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import Questions,Base
from schemas import QuestionBase
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
Base.metadata.create_all(bind=engine) 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]




@app.post("/questions")
async def create_questions(questions: QuestionBase,db:db_dependency):
    db_question = Questions(question_text=questions.question_text,choice_one=questions.choice_one,choice_two=questions.choice_two,choice_three=questions.choice_three,choice_four=questions.choice_four,correct_choice=questions.correct_choice)
    db.add(db_question)
    print(questions.question_text)
    
    db.commit()
    db.refresh(db_question)
    return True

@app.get("/view_questions")
def view_question(db: db_dependency,skip: int=0 ,limit: int=0):
   return db.query(Questions).offset(skip).limit(limit).all()
   








