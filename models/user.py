#!/usr/bin/python3
"""User Model Definition"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Init User instance"""
        super().__init__(*args, **kwargs)
        if 'email' in kwargs:
            self.email = kwargs['email']
        else:
            self.email = ""

        if 'password' in kwargs:
            self.password = kwargs['password']
        else:
            self.password = ""

        if 'first_name' in kwargs:
            self.first_name = kwargs['first_name']
        else:
            self.first_name = ""
            
        if 'last_name' in kwargs:
            self.last_name = kwargs['last_name']
        else:
            self.last_name = ""

