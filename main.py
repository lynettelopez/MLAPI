from typing import List
import models
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from ml import nlp
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from models import QuestionAnswerPair
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

class Article(BaseModel):
    content: str

class QuestionDelete(BaseModel):
    id: int

class QuestionUpdate(BaseModel):
    id: int
    question: str

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def read_main(request: Request, db: Session = Depends(get_db)):
    questions = db.query(QuestionAnswerPair)
    questions = questions.all()
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "questions": questions
    })

@app.post("/article")
async def analyze_article(article : Article,  db: Session = Depends(get_db)):
    nlp.clear()
    doc = nlp.consume_text(article.content)
    nlp.print()

    for qa_pair in nlp.qa_pairs:
        question_answers = QuestionAnswerPair()
        question_answers.message = article.content
        question_answers.question = qa_pair['question']
        question_answers.answer = qa_pair['answer']
        db.add(question_answers)
        db.commit()

    return {"message": article.content, "questions": nlp.qa_pairs}

@app.delete("/article")
async def delete_question(question: QuestionDelete,  db: Session = Depends(get_db)):
    db.execute(f"DELETE FROM questions WHERE id ={question.id}")
    db.commit()
    return {"id": question.id}

@app.update("/article")
async def update_question(question: QuestionUpdate,  db: Session = Depends(get_db)):
    pass








"""
@app.post("/article/")
async def analyze_article(articles : List[Article]):
    '''
    Analyze an article and extract entities with ✨ spacy ✨

    Statistical models  *will* have **errors.**
    * Extract entities
    * Scream Comments
    '''
    ents = []
    comments =  []
    for article in articles:
        for comment in article.comments:
            comments.append(comment.upper())
        doc = nlp(article.content)
        for ent in doc.ents:
            ents.append({"text": ent.text, "label": ent.label_})
    return {"ents": ents, "comments": comments}







"""









#Samples

'''
# given a query
@app.get("/article/{article_id}")
def analyze_article(article_id: int, q: str = None):
    count = 0
    if q:
        doc = nlp(q)
        count = len(doc.ents)
    return {"article_id": article_id, "q": q, "count": count}

Single article  Post
@app.post("/article/")
async def analyze_article(article : Article):
    doc = nlp(article.content)
    ents = []
    for ent in doc.ents:
        ents.append({"text": ent.text, "label": ent.label_})
    return {"message": article.content, "comments": article.comments, "ents": ents}


'''
