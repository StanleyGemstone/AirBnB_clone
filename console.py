#!/usr/bin/python3
""" A command line processor for manipulate objects
    created from Base class and its various subclasses
"""

import cmd
import sys
import os
from models.base_model import BaseModel


class Console(cmd.Cmd):
    prompt = ""

    if sys.stdin.isatty():
        prompt = "(hbnb) "

    def preloop(self):
        """command to be excuted before cmdloop invocation"""
        if not sys.stdin.isatty():
            print("(hbnb)")

    def do_create(self, new_instance):
        """This method creates a new instance of BaseModel and
        saves it (to the file.json in the current dir)
        then prints out the id of the created instance.
        """
        if (new_instance):
            if (new_instance == "BaseModel"):
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("**class name missing **")

    def do_show(self, key):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex:(hbnb)$ show BaseModel 1234-1234-1234.
        """
        from models import storage
        if (key):
            key_list = key.split()
            length = len(key_list)
            if (key_list[0] == "BaseModel"):
                if (length == 2):
                    delim = "."
                    get_obj = delim.join(key_list)
                    loader = storage.all()
                    obj = loader.get(get_obj, "** no instance found **")
                    print(obj)
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, key):
        """Delete an instance based on the class name and id
        (save the change into the JSON file).
        Ex: (hbnb)$ destroy BaseModel 1234-1234-1234.
        """
        from models import storage
        if (key):
            key_list = key.split()
            length = len(key_list)
            if (key_list[0] == "BaseModel"):
                if (length == 2):
                    delim = "."
                    get_obj = delim.join(key_list)
                    loader = storage.all()
                    obj = loader.get(get_obj, "** no instance found **")
                    if (obj != "** no instance found **"):
                        del loader[get_obj]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, cls_name):
        """ Prints all string representation of all instances based
        or not on the class name. Ex:(hbnb) $ all BaseModel or $
        """
        from models import storage
        to_list = []
        for obj in storage.all().values():
            to_list.append(obj.__str__())
        if (cls_name):
            if (cls_name == 'BaseModel'):
                print(to_list)
            else:
                print("** class doesn't exist **")
        else:
            print(to_list)

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

    def do_quit(self, line):
        """The quit command terminate the Console"""
        sys.exit(0)


if __name__ == '__main__':
    Console().cmdloop()
