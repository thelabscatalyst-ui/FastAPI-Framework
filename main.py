from  fastapi import FastAPI, HTTPException, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 
# from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# app is the object which is used to define all the routes

templates = Jinja2Templates(directory="templates")
# this is the directory where we will be storing our html files  

posts: list[dict] = [
    {
        "id": 1,
        "author": "Meher",
        "title": "My life",
        "image_path": "static/profile_pics/default.jpg",
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

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts})
    # Used the template file name that we are going to use
# this is basically home route 

@app.get("/posts")
def get_posts():
    return posts  
# this route will get the posts from the sample database
# when we are using a SQL database, we will use alchmey to fetch the data form there

@app.get("/posts/{id}") # this would tell that post id is part of the url 
def get_post(request: Request, id: int):
    for post in posts:
        if post["id"] == id:
            title = post["title"]
            return templates.TemplateResponse(request, "post.html", {"post": post, "title": title}) 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post was not found")
# this helps us to return the correct https status code 