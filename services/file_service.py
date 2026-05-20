import json
import os

class FileService:
    @staticmethod
    def load(filename):
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            return json.load(file)

    @staticmethod
    def save(filename, data):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)