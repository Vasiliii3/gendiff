from gendiff.formatter.constants import to_string
from gendiff.constants import SYMBOLS


def stylish(tree: list) -> str:
    def format_value(value, level):
        if isinstance(value, list):
            return walk(value, level + 4)
        else:
            return to_string(value)

    def walk(tree_, level=1):
        result = '{\n'
        empty = " " * level
        for string in tree_:
            diff, key, value = string
            diff = SYMBOLS[diff]
            formatted_value = format_value(value, level)
            result += f'{empty} {diff} {key}: {formatted_value}\n'
        result += " " * (level - 1) + "}"
        return result

    return walk(tree)
