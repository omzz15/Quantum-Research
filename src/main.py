import os
import importlib
from quantum_project import QuantumProject, create
from utils import validate_path_end

project : QuantumProject = None

def get_path():
    path = input("Please enter save path (leave blank for current): ")
    if not path:
        path = os.getcwd()
    return validate_path_end(path)

def get_name():
    return input("Please enter project name (leave blank to use current folder as name): ")

def handle_load():
    global project

    path = get_path()    
    path += get_name()

    project = QuantumProject(path) 

def handle_create():
    global project

    path = get_path()
    name = get_name()
    
    project = create(path, name)

def handle_init():
    i = input("load(l) or create(c) a project or exit(e): ")
    try:
        if i == 'l':
            action = "laod"
            handle_load()
        elif i == 'c':
            action = "create"
            handle_create()
        elif i == 'e':
            action = "exit"
            return False
        else:
            print("Options are 'l' to load a project, 'c' to create a project, or 'e' to exit")
            handle_init()
    except Exception as e:
        print(f"\nFailed to {action} project because:")
        print(e)
        print()
        handle_init()

    return True

def handle_command(command: str):
    if not command: return

    cmd, *args = command.split(" ", maxsplit=1)
    args = args[0].strip() if args else ""
    
    try:
        module = importlib.import_module(f".{cmd}", "commands")
    except:
        print(f"The command '{cmd}' is not valid. Try help for more information.")
        return
    
    try:
        module.invoke(project, args)
    except Exception as e:
        print(f"Unable to run the command {cmd} because:")
        print(e)
        print()

def main_loop():
    cmd = input(f"{project.name}:{project.path}> ")
    if cmd == "exit":
        project.save()
        return
    else:
        handle_command(cmd)
    main_loop()

if handle_init():
    main_loop()

print("Goodbye :)")