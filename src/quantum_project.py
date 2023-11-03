import json
import os

from utils import validate_path_end, remove_ending

current_project : 'QuantumProject' = None

def create(path : str, name : str | None):
    path = validate_path_end(path)
    full_path = validate_path_end(path + name)

    # get name from path if it is blank
    if not name:
        name = path[path.rfind("/") + 1:]

    os.makedirs(full_path, exist_ok=True)

    if len(os.listdir(full_path)) != 0:
        raise Exception(f"The directory {full_path} is not empty !!")

    data = {
        "name":name
    }
    
    return QuantumProject(full_path, data)

class QuantumProject:
    def __init__(self, path, data : dict | None = None):
        self.path = remove_ending(path,"/")
        self.load(data)

    def load(self, data : dict | None = None):
        if data:
            self.data = data
        else:
            try:
                with self.get_file("data.json") as f:
                    self.data = json.load(f)
            except Exception as e:
                raise Exception(f"The data.json file was unable to be loaded. The project may not be at {self.path} or is broken")
        self.name = self.data["name"]
    
    def get_file(self, relative_path : str, mode : str = 'r'):
        return open(self.path + "/" + relative_path, mode=mode)

    def save(self):
        with self.get_file("data.json", "w") as f:
            json.dump(self.data, f)