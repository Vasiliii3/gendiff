from gendiff.formatter.constants import to_str_python_to_json


def stylish(tree: list) -> str:
    def walk(tree_, level=1):
        result = '{\n'
        for string in tree_:
            emtpy = " " * level
            diff, key, value = string
            if isinstance(value, list):
                value = walk(value, level + 4)
                value += emtpy + "   }"
            else:
                value = to_str_python_to_json(value)
            result += f'{emtpy} {diff} {key}: {value}\n'
        return result

    return walk(tree) + "}"
