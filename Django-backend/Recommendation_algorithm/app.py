#Recommendation_algorithm/app.py
from flask import Flask,render_template,request
import pickle
import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import argparse
from functools import lru_cache
from pydantic import BaseModel

from management.popularity_recommender import popular_books_top
from management.collaborative_recommender import recommendFor
from management.search import search_book

import config 

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Book(BaseModel):
    name: str


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/hello")
def read_hello():
    return {"message": f"Hello from {get_settings().backend_name}"}


@app.get("/search/{book_name}")
async def search_book_name(book_name: str = ""):
    return search_book(book_name)


@app.get("/popular/{limit}")
async def get_popular(limit: int):
    return popular_books_top(limit)


@app.post("/recommend")
async def get_recommended(book: Book):
    print(book.name)
    recommendation_on = search_book(book.name, 1)[0]
    return {'book': recommendation_on, 'recommendation': recommendFor(book.name)}



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Book Recommender API")
    parser.add_argument("-e", "--env", default="dev")
    parser.add_argument("-w", "--workers", default=1, type=int)
    args = parser.parse_args()
    host = get_settings().backend_host
    port = get_settings().backend_port
    workers = args.workers

    if args.env == "dev":
        uvicorn.run(
            "app:app",
            host=host,
            port=port,
            reload=True,
            env_file="./config/.env.dev"
        )
    else:
        uvicorn.run(
            "app:app",
            host=host,
            port=port,
            env_file="./config/.env.prod",
            workers=workers,
        )


popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)

    return render_template('recommend.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)