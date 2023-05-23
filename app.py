from fastapi import FastAPI, HTTPException
from Models.article import Article
from uuid import uuid4 as uuid


app = FastAPI()

articles = [];

@app.get('/')
def read_root():
    return {"welcome": "Welcome to my REST"}

@app.get('/articles')
def get_articles():
    return articles

@app.post('/articles')
def save_articles(article: Article):
    article.id = str(uuid())
    articles.append(article.dict())
    return articles[-1]

@app.get('/article/{article_id}')
def get_article(article_id: str):
    for article in articles:
        if(article["id"] == article_id):
            return article
        
    raise HTTPException(status_code=404, detail="Article Not Found")


@app.delete('/article/{article_id}')
def delete_article(article_id: str):
    for index, article in enumerate(articles):
        if(article['id'] == article_id):
            articles.pop(index)
            return {"messagge" : "Article has been deleted succesfully"}
        else:
            raise HTTPException(status_code=404, detail="Article Not Found")
    
    raise HTTPException(status_code=404, detail="Article Not Found")
    
@app.put('/article/{article_id}')
def update_article(article_id:str, updatedArticle: Article):
    for index, article in enumerate(articles):
        if(article['id'] == article_id):
            #articles[index] = updatedArticle
            articles[index]["title"] = updatedArticle.title
            articles[index]["author"] = updatedArticle.author
            articles[index]["content"] = updatedArticle.content

            return {"messagge" : "Article has been updated succesfully"}
        else:
            raise HTTPException(status_code=404, detail="Article Not Found")
    
    raise HTTPException(status_code=404, detail="Article Not Found")

