from gendiff.parsing import open_file
from gendiff.formatter.style import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import styling_json
from gendiff.tree import walk

FORMAT = {'stylish': stylish,
          "plain": plain,
          "json": styling_json,
          }


def generate_diff(file_path1, file_path2, style):
    dict1 = open_file(file_path1)
    dict2 = open_file(file_path2)

    tree = walk(dict1, dict2)

    return FORMAT[style](tree)
