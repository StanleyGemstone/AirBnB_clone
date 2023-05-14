#!/usr/bin/python3
""" A command line processor for manipulate objects
    created from Base class and its various subclasses
"""

import cmd
import sys
import os
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
