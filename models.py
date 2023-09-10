from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    # Relationships
    tasks = relationship('Task', back_populates='user')
    time_entries = relationship('TimeEntry', back_populates='user')
    reports = relationship('Report', back_populates='user')

class Task(Base):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    # Relationships
    user = relationship('User', back_populates='tasks')
    time_entries = relationship('TimeEntry', back_populates='task')

class TimeEntry(Base):
    __tablename__ = 'time_entries'

    time_entry_id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.task_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime)
    duration_minutes = Column(Integer)

    # Relationships
    user = relationship('User', back_populates='time_entries')
    task = relationship('Task', back_populates='time_entries')

class Report(Base):
    __tablename__ = 'reports'

    report_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship
    user = relationship('User', back_populates='reports')
