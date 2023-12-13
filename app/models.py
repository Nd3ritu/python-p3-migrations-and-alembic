#!/usr/bin/env python3
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import (CheckConstraint, UniqueConstraint, Column, DateTime, Integer,String)
from sqlalchemy.orm import declarative_base

engine  = create_engine("sqlite:///migrations_test.db")
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        UniqueConstraint('email',
             name= "unique_email"),

        CheckConstraint('grade BETWEEN 1 AND 12',
             name='grade _between_1_and_12',)
    )

    id = Column(Integer(), primary_key= True)
    name = Column(String(), index = True)
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default = datetime.now())

    def __repr__(self):
        return f"Student {self.id}:"\
              + f"{self.name}"\
              + f"Grade: {self.grade}"
