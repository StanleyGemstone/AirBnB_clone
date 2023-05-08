# AirBnB_clone

## Welcome to the AirBnB clone project!

**Project description:**

This is the first step towards building our first full web application: the *AirBnB clone.* This first step is very important because we will be using what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

**Each task is linked and will help us to:**

- Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances

- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

- Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel

- Create the first abstracted storage engine of the project: File storage.

- Create all unittests to validate all our classes and storage engine

**Description of the command interpreter:**

The `console.py` will enable us to be able to manage the objects in the project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

**How to start and use console.py:**

Type `./console.py` in your terminal to launch the program in interative mode. After a prompt `(hbnb)` has been displayed, you can type help and press the enter button to see  all the available builtin commands to work with the objects.

```
$ ./console.py

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

To launch the program in non-interactive mode (like shell), see examples below:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
