#!/usr/bin/python3
"""
    A cmd application
"""
import cmd
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
                newIns = eval(line)
                newIns = newIns()
                storage.new(newIns)
                print(newIns.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        content = parse(line)
        if not content:
            print("** class name missing **")
        else:
            try:
                model = eval(content[0])  # check if the name of the class exist
                if len(content) < 2:
                    print("** instance id missing **")
                else:
                    instanceName = "{}.{}".format(content[0], content[1])
                    AvilableObj = storage.all()

                    if instanceName in AvilableObj:
                        print(model(**AvilableObj[str(instanceName)]))
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

    def do_all(self, line):  # TODO : the function always print the whole database not the specified class
        try:
            model = eval(line)
            items = []
            AvilableObj = storage.all()
            for key, val in AvilableObj.items():
                if model.__name__ in key:
                    items.append(model(**val).__str__())
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
                model = eval(content[0])  # check if the name of the class exist
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
                                model = model(**AvilableObj[instanceName])
                                modelDict = model.__dict__.copy()
                                
                                if content[2] in modelDict:
                                    kind = type(modelDict[content[2]])
                                    modelDict[content[2]] = kind(content[3].replace("\"",""))
                                else:
                                    modelDict[content[2]] = content[3].replace("\"","")

                                model.__dict__.update(modelDict)
                                storage.delete(instanceName)  # remove old obj from the DataBase
                                storage.new(model)  # Add the updated Item to the Database
                                storage.save()
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def default(self,line):
        try:
            eval(line)
        except:
            Place.all()


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

    def all(self):
        print("syntax : all <class_name> ")
        print("-- if exist print a list of string of all the class objects")


def parse(arg):
    return list(map(str, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
