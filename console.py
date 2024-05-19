#!/usr/bin/python3
""" Console or cmd Module for command interpreters"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from datetime import datetime
import re
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """AirBnB Command"""
    prompt = "(hbnb) "

    # TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def emptyline(self):
        """ empty """
        pass

    def do_EOF(self, line):
        """Exit console"""
        print()
        return True

    def do_quit(self, line):
        """Quit or exit command"""
        return True

    def help_quit(self):
        """Help rgument"""
        print("Quit command to exit the program\n")

    def handle_custom_command(self, class_name, action):
        """Handle custom  cmd"""
        parts = action.split("(")
        if len(parts) == 2 and parts[1].endswith(')'):
            action_name = parts[0]
            action_args = parts[1][:-1].split(',')

            # Remove quotes
            action_args = [arg.strip('\"') for arg in action_args]

            if action_name == 'show':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print(f"** no instance found **")
            elif action_name == 'all':
                instances = [
                    str(obj) for key, obj in storage.all().items()
                    if key.startswith(class_name + '.')
                ]
                print(instances)
            elif action_name == 'count':
                count = sum(
                    1 for key in storage.all()
                    if key.startswith(class_name + '.')
                )
                print(count)
            elif action_name == 'destroy':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print(f"** no instance found **")
            elif action_name == 'update':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    obj = storage.all()[key]
                    attribute_name = action_args[1]
                    attribute_value = action_args[2]

                    # Update the attribute.
                    setattr(obj, attribute_name, attribute_value)
                    obj.save()
                else:
                    print(f"** no instance found **")
            else:
                print(f"Unrecognized action: {action_name}.\
                Type 'help' for assistance.\n")
        else:
            print(f"Unrecognized action: {action}.\
            Type 'help' for assistance.\n")

    def default(self, line):
        """Handle other commands"""
        parts = line.split('.')
        if len(parts) == 2:
            class_name, action = parts
            self.handle_custom_command(class_name, action)
        else:
            print(f"Unrecognized command: {line}.\
                  Type 'help' for assistance.\n")

    def do_create(self, line):
        """Creates new instances"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.CLASSES:
            print("** class doesn't exist **")
            return
        
        try:
            object = self.CLASSES[class_name]()
            object.save()
            print(object.id)
        except Exception as e:
            print(e)

    def do_show(self, line):
        """Prints string"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])
        except Exception as e:
            print(e)
            
    def do_destroy(self, line):
        """Deletes instances"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
        except Exception as e:
            print(e)
        

    def do_all(self, line):
        """ Deletes instances
        """
        args = line.split()
        # objects = storage.all()

        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instances = [
                str(obj) for key, obj in storage.all().items()
                if key.startswith(class_name + '.')
            ]
            print(instances)

    def do_update(self, line):
        """Updates instances"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[key]

        if len(args) == 3:
            # Handle the dictionary
            try:
                attr_dict = eval(args[2])
                if isinstance(attr_dict, dict):
                    for attr_name, attr_value in attr_dict.items():
                        setattr(obj, attr_name, attr_value)
                    obj.save()
                else:
                    print("** dictionary format invalid **")
            except Exception as e:
                print("** dictionary format invalid **")
                print(e)
        elif len(args) == 4:
            # Handle attribute
            attr_name = args[2]
            attr_value = args[3]
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** attribute name or value missing **")

        

if __name__ == '__main__':
    HBNBCommand().cmdloop
