#!/usr/bin/python3
"""
    A cmd application
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_EOF(self, _):
        storage.save()
        print()
        return True

    def do_quit(self, _):
        storage.save()
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        else:
            try:
                newIns = eval(line)()
                newIns.save()
                print(newIns.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        content = parse(line)
        if not content:
            print("** class name missing **")
        else:
            try:
                # check if the name of the class exist
                model = eval(content[0])
                if len(content) < 2:
                    print("** instance id missing **")
                else:
                    instanceName = "{}.{}".format(content[0], content[1])
                    AvilableObj = storage.all()

                    if instanceName in AvilableObj:
                        print(AvilableObj[instanceName].__str__())
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        content = parse(line)
        if not content:
            print("** class name missing **")
        else:
            try:
                eval(content[0])  # check if the name of the class exist
                if len(content) < 2:
                    print("** instance id missing **")
                else:
                    instanceName = "{}.{}".format(content[0], content[1])
                    AvilableObj = storage.all()

                    if instanceName in AvilableObj:
                        storage.delete(instanceName)
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, line):
        try:
            items = []
            if line:
                eval(line)
                for key, val in storage.all().items():
                    if line in key:
                        items.append(val.__str__())
            else:
                for key, val in storage.all().items():
                    items.append(val.__str__())

            print(items)

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        content = parse(line)
        itemCount = len(content)

        if not content:
            print("** class name missing **")
        else:
            try:
                # check if the name of the class exist
                model = eval(content[0])
                if itemCount < 2:
                    print("** instance id missing **")
                else:
                    instanceName = "{}.{}".format(content[0], content[1])
                    AvilableObj = storage.all()

                    if instanceName in AvilableObj:
                        if itemCount < 3:
                            print("** attribute name missing **")
                        else:
                            if itemCount < 4:
                                print("** value missing **")
                            else:
                                model = AvilableObj[instanceName]
                                modelDict = model.__dict__.copy()

                                if content[2] in modelDict:
                                    kind = type(modelDict[content[2]])
                                    value = content[3].replace("\"", "")
                                    modelDict[content[2]] = kind(value)
                                else:
                                    value = content[3].replace("\"", "")
                                    modelDict[content[2]] = value

                                model.__dict__.update(modelDict)
                                # remove old obj from the DataBase
                                storage.delete(instanceName)
                                # Add the updated Item to the Database
                                storage.new(model)
                                storage.save()
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def default(self, line):
        """
            Will be used to handle the rest of the conditions

                result is a List containing the following:#
                    0 - the Class name
                    1 - the method we want to use
        """
        try:
            result = re.split(r'\.', line)
            model = globals()[result[0]]

            if (result[1] == "all()"):
                model.all()
            elif (result[1] == "count()"):
                model.count()
            elif ("show" in result[1]):
                id = re.match(r".*\.show\((.*)\)", line)[1]
                model.show(id)
            elif ("destroy" in result[1]):
                id = re.match(r".*\.destroy\((.*)\)", line)[1]
                model.destroy(id)
        except Exception as e:
            print("The command doesn't exist")

    "-------------------------------"
    "Documentation"
    "-------------------------------"

    def help_quit(self):
        print("syntax: quit")
        print("-- Exit the program")

    def help_EOF(self):
        print("syntax : Ctrl+d")
        print("-- Exit the program")

    def help_create(self):
        print("syntax : create <class_name> ")
        print("-- if exist a new instance of the class will be created")

    def help_show(self):
        print("syntax : show <class_name> <obj.id>")
        print("-- if exist print the string format of the obj")

    def help_all(self):
        print("syntax : all <class_name> ")
        print("-- if exist print a list of string of all the class objects")

    def help_destroy(self):
        print("syntax : destroy <class_name> <object_id> ")
        print("-- if exist remove the specified class object from database")

    def help_update(self):
        print("syntax : update <class_name> <object_id> <key> <value>")
        print("-- if exist update the class object with the new key/Value")


def parse(arg):
    return list(map(str, arg.split()))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
