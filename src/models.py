import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Relationship(Base):
    __tablename__ = 'relationship'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    followers_id = Column(String(250), nullable=False)
    following_id = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    post_type = Column(String(250), nullable=False)
    post_type_view = Column(String(250), nullable=False)
    post_date = Column(String(250), nullable=False)
    likes = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

class Feed(Base):
    __tablename__ = 'feed'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    feed_type = Column(String(250), nullable=False)
    feed_date = Column(String(250), nullable=False)
    likes = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

class Messages(Base):
    __tablename__ = 'messages'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    likes = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    state = Column(String(250), nullable=False)
    postal_code = Column(String(250), nullable=False)
    total_post = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')