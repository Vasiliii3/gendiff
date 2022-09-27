from gendiff.parsing import open_file
from gendiff.formatter.style import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import styling_json
from gendiff.tree import walk
from gendiff.formatter.constants import TYPE_FORMAT

FORMAT = {'stylish': stylish,
          "plain": plain,
          "json": styling_json,
          }


def generate_diff(file_path_one, file_path_two, style: str = 'stylish') -> str:
    if style not in TYPE_FORMAT:
        return f'format not supported. Supported {TYPE_FORMAT}'
    dict1 = open_file(file_path_one)
    dict2 = open_file(file_path_two)

    tree = walk(dict1, dict2)

    return FORMAT[style](tree)
