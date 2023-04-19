from fastapi import FastAPI, Depends, Request, Form
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session

import services
import models
from database import SessionLocal, engine


templates = Jinja2Templates(directory="templates")



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    recipes = db.query(models.Recipe).all()
    return templates.TemplateResponse("home.html",
                                       {"request": request, "recipes": recipes})
