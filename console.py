#!/usr/bin/python3
"""
Console module for the command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
