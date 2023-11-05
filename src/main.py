from typing import List, Annotated
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import Questions,Base,Users
from schemas import QuestionBase, QuestionSet,UsersBase
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
async def create_question(questionset: QuestionSet,db:db_dependency):
    for i in questionset.qset:
        print(i.question_text)
        db_question = Questions(id=i.id,question_text=i.question_text,choice_one=i.choice_one,choice_two=i.choice_two,choice_three=i.choice_three,choice_four=i.choice_four,correct_choice=i.correct_choice)
        print(db_question)
        db.add(db_question)
        db.commit()

    return True


@app.get("/view_questions")
def view_question(db: db_dependency,skip: int=0 ,limit: int=0):
   res=db.query(Questions).all()
   for i in res:
       yield i

@app.post("/evaluate")
async def evaluate(db: db_dependency, answers: dict ):
    score=0
    for i in answers:
        db_answer=db.query(Questions.correct_choice).where(Questions.id == int(i))
        r=db.scalar(db_answer)
        if answers[i] == r:
            score+=1
    return score
        
@app.post("/login")
async def authenticate(user_info: UsersBase,db: db_dependency):
    db_password=db.query(Users.password).where(Users.user_id==user_info.user_id)
    res=db.scalar(db_password)
    if user_info.password == res:
        return True
    else:
        
        return False