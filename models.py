
from sqlalchemy import Boolean, Column, ForeignKey, Numeric, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class QuestionAnswerPair(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    question = Column(String)
    answer = Column(String)