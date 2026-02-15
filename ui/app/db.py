import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ui.db")

# For simple dev usage we use SQLAlchemy sync engine. For production point DATABASE_URL to Postgres.
engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_engine():
    return engine

def get_session():
    return SessionLocal()
