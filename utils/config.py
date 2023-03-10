import json

class Config():
    def __init__(self, file_path):
        self.fileName = file_path

    def get(self, key:str):
        f = open(self.fileName)
        data = json.load(f)
        return data[key]