#!/usr/bin/python3
""" A command line processor for manipulate objects
    created from Base class and its various subclasses
"""

import cmd
import sys


class Console(cmd.Cmd):
    prompt = ""

    if sys.stdin.isatty():
        prompt = "(hbnb) "

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

    def do_quit(self, line):
        """The quit command terminate the Console"""
        sys.exit(0)


if __name__ == '__main__':
    Console().cmdloop()
