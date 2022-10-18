from gendiff.io import read_file
from gendiff.parsing import parse
from gendiff.formatter.style import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import styling_json
from gendiff.tree import walk
from gendiff.formatter.constants import TYPE_FORMAT, TYPE_FILE
import os.path

ERROR_TYPE = f'format file not supported. Supported {TYPE_FILE}'

FORMAT = {'stylish': stylish,
          "plain": plain,
          "json": styling_json,
          }

ERROR_FORMAT = f'format not supported. Supported {TYPE_FORMAT}'


def file_to_data(file):
    data = read_file(file)
    type_file = get_format(file)
    return parse(data, type_file)


def get_format(file):
    path, type_file = os.path.splitext(file)
    type_fle_without_point = type_file[1:]
    if type_fle_without_point not in TYPE_FILE:
        raise Exception(ERROR_TYPE)
    return type_fle_without_point


def generate_diff(file_path_one, file_path_two, style: str = 'stylish') -> str:
    if style not in TYPE_FORMAT:
        raise Exception(ERROR_FORMAT)
    data_file_one = file_to_data(file_path_one)
    data_file_two = file_to_data(file_path_two)

    tree = walk(data_file_one, data_file_two)

    return FORMAT[style](tree)
