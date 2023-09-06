from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    tasks = relationship('Task', back_populates='user')
    time_entries = relationship('TimeEntry', back_populates='user')
    reports = relationship('Report', back_populates='user')
