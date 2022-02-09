import os
import json

def read_files(directory_path):
    files = os.listdir(directory_path)
    data = []
    for file in files:
        with open(directory_path + "\\" + file) as json_file:
            data.append(json.load(json_file))
    return data