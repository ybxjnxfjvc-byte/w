from sqlalchemy import Column, BigInteger, String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    full_name = Column(String)
    username = Column(String, nullable=True)
    registered_at = Column(DateTime, default=datetime.utcnow)
    current_lesson = Column(Integer, default=0)
    is_admin = Column(Boolean, default=False)

class LessonProgress(Base):
    __tablename__ = "lesson_progress"
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    lesson_id = Column(Integer)
    score = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
