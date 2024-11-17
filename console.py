#!/usr/bin/python3
"""
Command interpreter for managing the AirBnB clone.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""
    prompt = "(hbnb) "

    def do_create(self, args):
        """Creates a new instance of a class."""
        if not args:
            print("** class name missing **")
            return
        if args not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[args]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Shows an instance of a class."""
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
            return
        if args_list[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return
        key = f"{args_list[0]}.{args_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance of a class."""
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
            return
        if args_list[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return
        key = f"{args_list[0]}.{args_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, args):
        """Shows all instances of a class or all classes."""
        if args and args not in classes:
            print("** class doesn't exist **")
            return
        obj_list = []
        for key, obj in storage.all().items():
            if not args or obj.__class__.__name__ == args:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, args):
        """Updates an instance of a class."""
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
            return
        if args_list[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return
        key = f"{args_list[0]}.{args_list[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args_list) == 2:
            print("** attribute name missing **")
            return
        if len(args_list) == 3:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args_list[2]
        attr_value = args_list[3]
        try:
            attr_value = eval(attr_value)
        except Exception:
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()

    def emptyline(self):
        """Does nothing on an empty line."""
        pass

    def do_quit(self, args):
        """Exits the program."""
        return True

    def do_EOF(self, args):
        """Exits the program."""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
