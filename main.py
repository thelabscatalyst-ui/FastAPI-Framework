from  fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
# app is the object which   is used to define all the routes

posts: list[dict] = [
    {
        "id": 1,
        "author": "Meher",
        "title": "My life",
        "content": "Hi guys, i am using this content for learning the fastapi framework",
        "date": "19th April, 2026" 
    },
    {
        "id": 2,
        "author": "Arjun",
        "title": "His life",
        "content": "Hi guys, i am also using this content for learning the fastapi framework",
        "date": "24th April, 2026 " 
    },
] #this is basically a sample database that i am using to create a sample page 

@app.get("/", response_class=HTMLResponse)
def home():
    return f"<h1> Welcome to {posts[0]['title']} <h1>"
# this is basically home route 

@app.get("/posts")
def get_posts():
    return posts  
# this route will get the posts from the sample database
# when we are using a SQL database, we will use alchmey to fetch the data form there