from typing import List

from fastapi import FastAPI
from ml import nlp
from pydantic import BaseModel


class Article(BaseModel):
    content: str
    comments: List[str] = []

app = FastAPI()

@app.get("/")
def read_main():
    return {"message": "Hello World"}

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
