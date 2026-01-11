#!/usr/bin/python3
"""
Module for the HBNB console
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for AirBnB clone
    """
    prompt = '(hbnb) '
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class, saves it and prints the id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = self.__classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        elif args[0] in self.__classes:
            for key, obj in storage.all().items():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_val = args[3]

        try:
            if hasattr(obj, attr_name):
                attr_type = type(getattr(obj, attr_name))
                setattr(obj, attr_name, attr_type(attr_val))
            else:
                setattr(obj, attr_name, attr_val)
        except ValueError:
            pass
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
