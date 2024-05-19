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
    __file_path = 'file.json'  # path to file
    __objects = {}  # storage dictionary

    def all(self):
        """Returns stored models' dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object with the key"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads dictionary from JSON file"""

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
