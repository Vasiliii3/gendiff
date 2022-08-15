import json
import yaml
from yaml.loader import SafeLoader


def open_file(file):
    with open(file, 'r') as fp:
        type_file = file.split(".")[1]
        if type_file == "json":
            file_ = json.load(fp)
        elif type_file == "yml" or "yaml":
            file_ = yaml.load(fp, Loader=SafeLoader)
        return file_
