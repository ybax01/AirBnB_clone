#!/usr/bin/python3
"""
Command interpreter module for AirBnB clone.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone."""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_EOF(self, arg):
        """Handles EOF to exit the program."""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_all(self, arg):
        """Retrieve all instances of a specified class or all objects.

        Usage:
            all <class name>
            <class name>.all()
        """
        if "." in arg and arg.endswith(".all()"):
            class_name = arg.split(".")[0]
        else:
            class_name = arg

        if class_name and class_name not in self.classes:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        result = []

        if class_name:
            for key, obj in all_objs.items():
                if key.startswith(class_name):
                    result.append(str(obj))
        else:
            result = [str(obj) for obj in all_objs.values()]

        print(result)

    def default(self, line):
        """Handle commands not explicitly defined."""
        if line.endswith(".all()"):
            self.do_all(line)
        else:
            print("** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
