from gendiff.parsing import open_file
from gendiff.formatter.style import stylish
from gendiff.tree import walk


def generate_diff(file_path1, file_path2, style):
    dict1 = open_file(file_path1)
    dict2 = open_file(file_path2)

    tree = walk(dict1, dict2)

    if style == "stylish":
        return stylish(tree)
