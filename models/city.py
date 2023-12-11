#!/usr/bin/python3
""" Class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """Init City instance"""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get("name", "")
