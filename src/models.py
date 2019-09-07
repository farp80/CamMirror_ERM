import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Membership(Base):
    __tablename__ = 'membership'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Profiles(Base):
    __tablename__ = 'profiles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    date = Column(String(250), nullable=False)
    membership_id = Column(Integer, ForeignKey('membership.id'))
    user_id = Column(Integer, ForeignKey('users.id'))


class Pictures(Base):
    __tablename__ = 'pictures'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    updated_date = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')