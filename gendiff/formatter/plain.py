from gendiff.constants import ADDED, REMOVED, CHANGED2, UNCHANGED
from gendiff.formatter.constants import to_str_python_to_json

BEFORE = 'Property'


def key_to_string(value):
    if isinstance(value, list):
        return '[complex value]'
    elif value is None or isinstance(value, bool):
        return to_str_python_to_json(value)
    elif isinstance(value, int):
        return value
    return f"'{value}'"


def plain(tree: list) -> str: # noqa: max-complexity: 8
    def walk(tree_, way):
        result = ''
        for count, nodes in enumerate(tree_, 0):
            diff, key, value = nodes
            way_ = f'{way}{key}'
            if diff == UNCHANGED and isinstance(value, list):
                result += walk(value, f'{way_}.')
            value = key_to_string(value)
            if diff == CHANGED2:
                old_value = key_to_string(tree_[count - 1][2])
                result += f"{BEFORE} '{way_}' was updated. " \
                          f"From {old_value} to {value}\n"
            elif diff == ADDED:
                result += f"{BEFORE} '{way_}' was added with value: {value}\n"
            elif diff == REMOVED:
                result += f"{BEFORE} '{way_}' was removed\n"

        return result

    return walk(tree, way='')[:-1]
