#!/usr/bin/python3
import uuid
from datetime import datetime
"""
BaseModel - a class that defines all common
attributes/methods for other classes.
"""


class BaseModel:
    """
    BaseModel - a class that defines all common
    attributes/methods for other classes.

    Public instance attributes:
    id: string assigned with an uuid.
    created_at: datetime assigned with the current datetime (at creation).
    updated_at: datetime - assign with the current datetime (at update).

    Public instance methods:
    save(self): updates the public instance attribute
                updated_at with the current datetime
    to_dict(self): returns a dictionary containing
                all keys/values of __dict__ of the instance.
    """
    def __init__(self):
        """ __init__ - set up the initial state of an object."""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ save - updates the public instance attribute
            updated_at with the current datetime"""
        updated_at = datetime.now()

    def to_dict(self):
        """ to_dict - returns a dictionary containing
            all keys/values of __dict__ of the instance"""
        _dict = self.__dict__.copy()
        _dict["__class__"] = self.__class__.__name__
        for key, value in _dict.items():
            if isinstance(value, datetime):
                _dict[key] = value.isoformat()

        return _dict

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"
