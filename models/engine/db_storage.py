#!/usr/bin/python3
"""
New engine DBStorage
models/ engine/ db_storage.py
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from pprint import pprint


class DBStorage:
    """
    New engine DBStorage
    models/ engine/ db_storage.py
    """

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            metadata = MetaData()
            metadata.reflect(self.__engine)
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        i will comeback here
        this one is one tough beast
        """
        data = {}
        tables = [User, State, City, Amenity, Place, Review]
        for table in tables:
            objs = self.__session.query(table).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                data[key] = obj
        return data

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        create the current database session
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """close"""
        self.reload()
