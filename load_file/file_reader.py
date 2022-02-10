import os
import json
from logs.logging import info_log, debug_log, warning_log, error_log

def read_files(directory_path):
    info_log(__name__, read_files.__name__, "Entered into the function")
    files = os.listdir(directory_path)
    data = []
    for file in files:
        try:
            with open(directory_path + "\\" + file) as json_file:
                data.append(json.load(json_file))
        except:
            error_log(__name__, read_files.__name__, "No such file or directory")
            break
    info_log(__name__, read_files.__name__, "The function ended successfully")
    return data