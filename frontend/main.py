from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("base.html", {
        "request": request,
        "latest_post": {
            "title": "Your latest post",
            "date": "2024-03-21",
            "excerpt": "Post preview..."
        },
        "latest_project": {
            "title": "Your latest project",
            "description": "Project description",
            "technologies": ["Python", "FastAPI", "AI"]
        }
    })
@app.get("/portfolio")
def portfolio(request: Request):
    return templates.TemplateResponse("portfolio.html", {"request": request})
