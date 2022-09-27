from gendiff.formatter.constants import replacement


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
                value = replacement(value)
            result += f'{emtpy} {diff} {key}: {value}\n'
        return result

    return walk(tree) + "}"
