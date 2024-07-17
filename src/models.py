import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#Tabla de usuarios 
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)

    #RELACIÓN de la tabla users con favourites
    favourites = relationship("Favourites", back_populates="users")

    
#Tabla de personajes
#En la columna gender le aporto un dato tipo Enum:
#Hace que solo se pueda elegir entre las 3 opciones proporcionadas,
#que en este caso son male, female y others
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

    #RELACIÓN de la tabla characters con favourites
    favourites = relationship("Favourites", back_populates="characters")

#Tabla de planetas
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

    #RELACIÓN de la tabla planets con favourites
    favourites = relationship("Favourites", back_populates="planets")

#Tabla de vehículos
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

    #RELACIÓN de la tabla starhips con favourites
    favourites = relationship("Favourites", back_populates="starships")

#Tabla favoritos
#en esta tabla se añaden 4 columnas que hacen referencia al id de:
#planetas, vehiculos, personajes y usuarios
class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    starships_id = Column(Integer, ForeignKey('starships.id'), nullable=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    #Con back_populates, se debe crear explícitamente la RELACIÓN tanto en la clase favourites como en la clases users, starships, planets y characters:
    #Creando las RELACIONES de la tabla favourites con users, starships, planets y characters
    users = relationship("Users", back_populates="favourites")
    starships = relationship("Starships", back_populates="favourites")
    planets = relationship("Planets", back_populates="favourites")
    characters = relationship("Characters", back_populates="favourites")



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
