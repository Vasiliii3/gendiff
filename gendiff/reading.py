import json
import yaml
from yaml.loader import SafeLoader


def open_file(file, type_file):
    with open(file, 'r') as fp:
        if type_file == "json":
            file_ = json.load(fp)
        elif type_file == "yml" or "yaml":
            file_ = yaml.load(fp, Loader=SafeLoader)
        return file_
