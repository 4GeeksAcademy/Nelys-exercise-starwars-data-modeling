import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    apellidos = Column(String(50))
    email = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(Integer)
    gender = Column(String(50))
    created = Column(Integer)
    edited = Column(String(50))
    homeworld = Column(String(50))
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(50))
    population = Column(Integer)
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(Integer)
    created = Column(String(50))
    edited = Column(String(50))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    model = Column(String(50))
    vehicle_class = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew= Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(50))
    films = Column(String(50))
    pilots = Column(String(50))
    created = Column(String(50))
    edited = Column(String(50))

class Favorites_Planets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship(Usuarios)

class Favorites_People(Base):
    __tablename__ = 'favorites_people'
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship(Usuarios)

class Favorites_Vehicles(Base):
    __tablename__ = 'favorites_vehicles'
    id = Column(Integer, primary_key=True)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)
    usuario = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship(Usuarios)

def to_dict(self):
    return {}
    




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
