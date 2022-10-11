from gendiff.formatter.constants import to_string
from gendiff.constants import SYMBOLS


def stylish(tree: list) -> str:
    def walk(tree_, level=1):
        result = '{\n'
        emtpy = " " * level
        for string in tree_:
            diff, key, value = string
            diff = SYMBOLS[diff]
            if isinstance(value, list):
                value = walk(value, level + 4)
            else:
                value = to_string(value)
            result += f'{emtpy} {diff} {key}: {value}\n'
        result += " " * (level - 1) + "}"
        return result

    return walk(tree)
