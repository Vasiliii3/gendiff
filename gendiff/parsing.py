import os.path
from gendiff.formatter.constants import TYPE_FILE

ERROR_TYPE = f'format file not supported. Supported {TYPE_FILE}'

def parsing_type_file(file):
    path, type_file = os.path.splitext(file)
    type_fle_without_point = type_file[1:]
    if type_fle_without_point not in TYPE_FILE:
        raise Exception(ERROR_TYPE)
    return type_fle_without_point