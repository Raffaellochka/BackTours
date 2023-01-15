from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, Column, Relationship, SQLModel

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:kent95@127.0.0.1:5432/tournaments"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()