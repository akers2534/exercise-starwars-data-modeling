import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    films_id = Column(Integer, ForeignKey("films.id"), nullable=False)
    species_id = Column(Integer,ForeignKey("species.id"), nullable=False)
    starships_id = Column(Integer,ForeignKey("starships.id"), nullable=False)
    vehicles_id = Column(Integer,ForeignKey("vehicles.id"), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    episode_id = Column(String(250), nullable=False)
    opening_crawl = Column(String(250), nullable=False)
    director = Column(String(250), nullable=False)
    producer = Column(String(250), nullable=False)
    release_date = Column(String(250), nullable=False)
    characters_id = Column(Integer, ForeignKey("people.id"), nullable=False)
    planets_id = Column(Integer, ForeignKey("planets.id"), nullable=False)
    species_id = Column(Integer, ForeignKey("species.id"), nullable=False)
    starships_id = Column(Integer, ForeignKey("starships.id"), nullable=False)
    vehicles_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)


class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    starships_class= Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    hyperdrive_rating = Column(String(250), nullable=False)
    mglt = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    films_id = Column(Integer, ForeignKey("films.id"), nullable=False) 
    pilots_id = Column(Integer, ForeignKey("pilots.id"), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)

     

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    films_id = Column(Integer, ForeignKey("films.id"), nullable=False) 
    pilots_id = Column(Integer, ForeignKey("pilots.id"), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)





class Species(Base):
    __tablename__ = 'Species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(250), nullable=False)
    designation = Column(String(250), nullable=False)
    average_height = Column(String(250), nullable=False)
    average_lifespan = Column(String(250), nullable=False)
    eye_colors = Column(String(250), nullable=False)
    hair_colors = Column(String(250), nullable=False)
    skin_colors = Column(String(250), nullable=False)
    language = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    people = Column(Integer, ForeignKey("people.id"), nullable=False)
    films = Column(Integer, ForeignKey("films.id"), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    residents = Column(Integer, ForeignKey("residents.id"), nullable=False)
    films = Column(Integer, ForeignKey("films.id"), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)






## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
