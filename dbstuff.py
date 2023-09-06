from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base


engine = create_engine('sqlite:///taskmonitor.db')
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
