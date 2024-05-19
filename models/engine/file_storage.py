#!/usr/bin/python3

"""
manage file storage for hbnb clone
by serialization of instances
"""

import json
from models.base_model import BaseModel
from os import path
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """ Manage storage of bnb models in JSON file format"""
   
    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    __file_path = "file.json"  # path to file
    __objects = {}  # dictionary

    def all(self):
        """Returns objects"""
        return self.__objects

    def new(self, obj):
        """Sets new objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save objects to file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the file to objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                serialized_objects = json.load(file)
                for key, obj_data in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    # creates instances
                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**obj_data)
                    # Store instances
                    self.__objects[key] = obj_instance

    
