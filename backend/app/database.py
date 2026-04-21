from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


# connect with db
engine = create_engine(
    settings.database_url,
    connect_args ={"check_same_thread": False}
)

# create session
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# base class for models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind = engine)