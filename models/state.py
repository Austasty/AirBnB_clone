#!/usr/bin/python3
"""State Model Definition"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Init State instance"""
        super().__init__(*args, **kwargs)
        self.name = ""
