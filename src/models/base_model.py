from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import Config

engine = create_engine(Config.DB_PATH)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()