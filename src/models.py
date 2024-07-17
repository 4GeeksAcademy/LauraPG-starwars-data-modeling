import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)

    favourites = relationship("Favourites", back_populates="users")

    

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    birth_year = Column(String(10))
    gender = Column(Enum('male', 'female', 'others', name='gender'))

    favourites = relationship("Favourites", back_populates="characters")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(50))
    population = Column(Integer)
    climate = Column(String(50))
    terrain = Column(String(50))

    favourites = relationship("Favourites", back_populates="planets")


class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    model = Column(String(150))
    starship_class = Column(String(150))
    manufacturer =  Column(String(150))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)

    favourites = relationship("Favourites", back_populates="starships")


class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    starships_id = Column(Integer, ForeignKey('starships.id'), nullable=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    users = relationship("Users", back_populates="favourites")
    starships = relationship("Starships", back_populates="favourites")
    planets = relationship("Planets", back_populates="favourites")
    characters = relationship("Characters", back_populates="favourites")



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
