#!/usr/bin/python3
"""FileStorage Module"""

import json
import os




class FileStorage:
    """Definition of FileStorage Class"""
    
    __file_path = "file.json"
    __objects = {}
    __class_modules = {
        "BaseModel": "models.base_model",
        "User": "models.user",
        "Place":"models.place", 
        "State": "models.state", 
        "City":"models.city", 
        "Amenity":"models.amenity",
        "Review" : "models.review"
    }
    classes = {"BaseModel": "models.base_model",
        "User": "User",
        "Place":"Place", 
        "State": "State", 
        "City":"City", 
        "Amenity":"Amenity",
        "Review" : "Review"}
    
    def import_class(cls, class_name):
        """Dynamically imports and returns the specified class."""
        module_path = cls.__class_modules.get(class_name)
        if module_path:
            module = __import__(module_path, fromlist=[class_name])
            return getattr(module, class_name)
        else:
            raise ImportError(f"Class '{class_name}' not found in __class_modules.")
    
    def all(self) -> dict:
        """ returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj
    
    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)
          
    def reload(self):
        """ 
        deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists; 
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r") as json_file:
                    json_data = json.load(json_file)

                    if isinstance(json_data, dict):
                        for key, value in json_data.items():
                            class_name, obj_id = key.split('.')
                            # Import BaseModel locally here
                            obj_class = self.import_class(class_name)
                            obj_instance = obj_class(**value)
                            FileStorage.__objects[key] = obj_instance

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print(f"File not found: {FileStorage.__file_path}")

                
                
        
        