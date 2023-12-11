#!/usr/bin/python3
"""
Console module for the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        print("Bye!")
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("Bye!")
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a specified
           class, saves it, and prints the id """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]

        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        # Use import_class to get the actual class
        class_instance = storage.import_class(class_name)()

        # Continue with your existing logic
        class_instance.save()
        print(class_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args or args[0] not in storage.classes:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
        else:
            print(instances[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args or args[0] not in storage.classes:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
        else:
            del instances[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        instances = storage.all()
        args = arg.split()

        if not args:
            print([str(obj) for obj in instances.values()])
            return

        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        print(
            [
                str(obj)
                for key, obj in instances.items()
                if key.split('.')[0] == args[0]
            ]
        )

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args or args[0] not in storage.classes:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return


        instance = instances[key]
        attribute_name = args[2]
        attribute_value = args[3]

        setattr(instance, attribute_name, eval(attribute_value))
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
