#!/usr/bin/python3
"""
Command interpreter for HBNB project.
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB console.
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        Usage: create <class name>
        """
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        instance = self.classes[args]()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance.
        Usage: show <class name> <id>
        """
        tokens = args.split()
        if not tokens:
            print("** class name missing **")
            return
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = f"{tokens[0]}.{tokens[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, args):
        """
        Deletes an instance based on class name and id.
        Usage: destroy <class name> <id>
        """
        tokens = args.split()
        if not tokens:
            print("** class name missing **")
            return
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = f"{tokens[0]}.{tokens[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """
        Prints all string representations of instances.
        Usage: all or all <class name>
        """
        objects = storage.all()
        if args:
            if args not in self.classes:
                print("** class doesn't exist **")
                return
            instances = [str(obj) for key, obj in objects.items() if key.startswith(args)]
        else:
            instances = [str(obj) for obj in objects.values()]
        print(instances)

    def do_update(self, args):
        """
        Updates an instance by adding/updating an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        tokens = args.split()
        if not tokens:
            print("** class name missing **")
            return
        if tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        key = f"{tokens[0]}.{tokens[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        if len(tokens) < 3:
            print("** attribute name missing **")
            return
        if len(tokens) < 4:
            print("** value missing **")
            return
        attr_name = tokens[2]
        attr_value = tokens[3].strip('"')
        if attr_name not in {"id", "created_at", "updated_at"}:
            # Cast value to the appropriate type
            if attr_value.isdigit():
                attr_value = int(attr_value)
            else:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    pass
            setattr(instance, attr_name, attr_value)
            instance.save()

    def do_EOF(self, arg):
        """
        Handles EOF (Ctrl+D) to exit the program.
        """
        print()
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Overrides default behavior for empty input.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
