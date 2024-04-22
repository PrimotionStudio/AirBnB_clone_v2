#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
import models
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from sqlalchemy import *


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(50),
                             ForeignKey("amenties.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        review = relationship("Review", cascade="delete", backref="place")
        amenities = relationship("Amenity",
                                 secondary="place_amenities",
                                 viewonly=False)
    elif getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def reviews(self):
            """
            returns the list of Review instances with
            place_id equals to the current Place.id
            """
            _reviews = models.storage.all(Review)
            revs = []
            for i in _reviews.values():
                if i.place_id == self.id:
                    revs.append(i)
            return revs

        @property
        def amenities(self):
            """
            returns the list of Amenity instances
            based on the attribute amenity_ids that
            contains all Amenity.id linked to the Place
            """
            _amenities = models.storage.all(Amenity)
            _amen = []
            for i in _amenities.values():
                if i.id in self.amenity_ids:
                    _amen.append(i)
            return _amen

        @amenities.setter
        def amenities(self, obj=None):
            if obj and isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
