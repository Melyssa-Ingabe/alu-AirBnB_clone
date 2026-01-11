# AirBnB Clone - The Console

This is the first step towards building a full web application: the AirBnB clone. This repository contains the command interpreter (console) for managing AirBnB objects.

## Description
The command interpreter is a tool to manage the objects of our project. It allows you to:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc.
- Do operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy an object

## Installation
To clone and use this repository, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/nshderrick056/alu-AirBnB_clone.git
   ```
2. Navigate to the directory:
   ```bash
   cd alu-AirBnB_clone
   ```

## Requirements
- All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.8.*)
- All your files must be executable
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

## How to use
The console can be used in both interactive and non-interactive modes.

### Interactive Mode
Run the console:
```bash
./console.py
```
At the prompt `(hbnb)`, you can type commands:
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF      all  create  destroy  help  quit  show  update

(hbnb) create User
0e0d867c-17e0-4740-9b4f-83266937e193
(hbnb) show User 0e0d867c-17e0-4740-9b4f-83266937e193
[User] (0e0d867c-17e0-4740-9b4f-83266937e193) {'id': '0e0d867c-17e0-4740-9b4f-83266937e193', 'created_at': datetime.datetime(2025, 1, 11, 16, 45, 0, 123456), 'updated_at': datetime.datetime(2025, 1, 11, 16, 45, 0, 123456)}
(hbnb) quit
```

### Non-Interactive Mode
Pipe commands into the console:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF      all  create  destroy  help  quit  show  update

$ echo "create BaseModel" | ./console.py
(hbnb) bdb6ef72-68c4-4b52-9b0d-45300f8627b4
(hbnb)
```

## Testing
All tests are located in the `tests` folder and can be executed using the `unittest` module.

Run all tests:
```bash
python3 -m unittest discover tests
```

To run a specific test file:
```bash
python3 -m unittest tests/test_models/test_base_model.py
```

## Authors
Created by [nshut](https://github.com/nshderrick056)
