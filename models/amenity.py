from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that inherits from he BaseModel"""

    def __init__(self, *args, **kwargs):
        """Init Amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = ""
