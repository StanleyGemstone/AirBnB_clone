#!/usr/bin/python3
""" A command line processor for manipulate objects
    created from Base class and its various subclasses
"""

import cmd
import sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    if sys.stdin.isatty():
        prompt = "(hbnb) "
    class_dic = [
                    "BaseModel",
                    "User",
                    "Place",
                    "State",
                    "City",
                    "Amenity",
                    "Review"
    ]

    def preloop(self):
        """command to be excuted before cmdloop invocation"""
        if not sys.stdin.isatty():
            print("(hbnb)")

    def postcmd(self, stop, line):
        """handle post cmd command during isatty"""
        if not sys.stdin.isatty():
            print("(hbnb) ", end='')
        return stop

    def emptyline(self):
        """handler for empty argument"""
        pass

    def do_EOF(self, line):
        """handle for EOF signal"""
        "Exit"
        return True

    def do_create(self, line):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_quit(self, line):
        """The quit command terminate the Console"""
        sys.exit(0)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
