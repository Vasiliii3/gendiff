import os.path
import json
import yaml
from gendiff.formatter.constants import TYPE_FILE

ERROR_TYPE = f'format file not supported. Supported {TYPE_FILE}'

PARSERS = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "yml": yaml.safe_load,
}


def parsing_type_file(file):
    path, type_file = os.path.splitext(file)
    type_fle_without_point = type_file[1:]
    if type_fle_without_point not in TYPE_FILE:
        raise Exception(ERROR_TYPE)
    return type_fle_without_point


def data_to_dict(data, file):
    type_file = parsing_type_file(file)
    return PARSERS[type_file](data)
