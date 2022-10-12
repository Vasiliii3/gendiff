from gendiff.io import read_file
from gendiff.parsing import data_to_dict
from gendiff.formatter.style import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import styling_json
from gendiff.tree import walk
from gendiff.formatter.constants import TYPE_FORMAT

FORMAT = {'stylish': stylish,
          "plain": plain,
          "json": styling_json,
          }

ERROR_FORMAT = f'format not supported. Supported {TYPE_FORMAT}'


def generate_diff(file_path_one, file_path_two, style: str = 'stylish') -> str:
    if style not in TYPE_FORMAT:
        raise Exception(ERROR_FORMAT)
    data_file_one = data_to_dict(read_file(file_path_one), file_path_one)
    data_file_two = data_to_dict(read_file(file_path_two), file_path_two)

    tree = walk(data_file_one, data_file_two)

    return FORMAT[style](tree)
