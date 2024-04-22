#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="delete", backref="state")

    if getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def cities(self):
            """
            returns the list of City instances with
            state_id equals to the current State.id
            """
            _cities = []
            for city in models.storage.all(City):
                if city.state_id == self.id:
                    _cities.append(city)
            return _cities
