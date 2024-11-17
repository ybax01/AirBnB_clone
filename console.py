#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB console.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        Usage: Ctrl+D
        """
        print()
        return True

    def emptyline(self):
        """
        Overrides the default behavior of repeating the last command.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
