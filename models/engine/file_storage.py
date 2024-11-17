#!/usr/bin/python3
"""
FileStorage module
Defines a class to serialize and deserialize objects.
"""
import json


class FileStorage:
    """Serializes and deserializes JSON files for object persistence"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects in the storage"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file into __objects"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name = value["__class__"]
                if cls_name == "BaseModel":
                    self.__objects[key] = BaseModel(**value)
                elif cls_name == "User":
                    self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
