import uuid
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import methods, models, schemas
from database import SessionLocal, engine
from sqlmodel import Field, Column, Relationship, SQLModel
from fastapi.middleware.cors import CORSMiddleware

SQLModel.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/tours/", response_model=List[schemas.TourView])
def read_tours(db: Session = Depends(get_db)):
    users = methods.get_tours(db)
    return users


@app.get("/parts/{id}", response_model=List[schemas.PartView])
def read_parts(id: uuid.UUID, db: Session = Depends(get_db)):
    users = methods.get_participants_by_tour(db, id)
    return users


@app.get("/teams/{id}", response_model=schemas.TeamView)
def read_teams(id: uuid.UUID, db: Session = Depends(get_db)):
    users = methods.get_team_by_part(db, id)
    return users


@app.get("/users/{id}", response_model=schemas.UserView)
def read_users(id: uuid.UUID, db: Session = Depends(get_db)):
    users = methods.get_user_by_part(db, id)
    return users


@app.get("/comleted/{id}", response_model=List[schemas.ComView])
def read_coms(id: uuid.UUID, db: Session = Depends(get_db)):
    users = methods.get_completed_by_part(db, id)
    return users


@app.get("/task/{id}", response_model=List[schemas.TaskView])
def read_task(id: uuid.UUID, db: Session = Depends(get_db)):
    users = methods.get_task_by_guid(db, id)
    return users


@app.get("/medium-task-value/", response_model=schemas.MediumTaskView)
def read_task(db: Session = Depends(get_db)):
    users = methods.get_medim_tasks(db)
    return users


@app.get("/medium-prize-value/", response_model=schemas.MediumPrizeView)
def read_task(db: Session = Depends(get_db)):
    users = methods.get_medim_prize(db)
    return users
