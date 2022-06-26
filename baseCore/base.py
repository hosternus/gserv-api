from config import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Engine = create_engine(DATABASE_URI, echo=False)
Session = sessionmaker(bind=Engine, autocommit=False, autoflush=False)()
Base = declarative_base()
