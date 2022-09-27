from gendiff.formatter.constants import replacement

BEFORE = 'Property'


def replacement_value(value):
    if isinstance(value, list):
        return '[complex value]'
    elif value is None or isinstance(value, bool):
        return replacement(value)
    return f"'{value}'"


def plain(tree: list) -> str: # noqa: max-complexity: 8
    def walk(tree_, way):
        result = ''
        for count, nodes in enumerate(tree_, 0):
            diff, key, value = nodes
            way_ = f'{way}{key}'
            if diff == " " and isinstance(value, list):
                result += walk(value, f'{way_}.')
            value = replacement_value(value)
            if (count + 1) != len(tree_) and key == tree_[count + 1][1]:
                new_value = replacement_value(tree_[count + 1][2])
                result += f"{BEFORE} '{way_}' was updated. " \
                          f"From {value} to {new_value}\n"
                continue
            if diff == "+" and key != tree_[count - 1][1]:
                result += f"{BEFORE} '{way_}' was added with value: {value}\n"
            if diff == "-":
                result += f"{BEFORE} '{way_}' was removed\n"

        return result

    return walk(tree, way='')[:-1]
