#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
import os

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)

    # Check if the database file was created
    if os.path.exists('students.db'):
        print("Database 'students.db' created successfully.")
    else:
        print("Failed to create the database.")
