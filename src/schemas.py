from pydantic import BaseModel
from typing import List



class QuestionBase(BaseModel):
    id: int
    question_text: str
    choice_one: str
    choice_two: str
    choice_three: str
    choice_four: str
    correct_choice: str

class QuestionSet(BaseModel):
    qset: List[QuestionBase]
