from gendiff.constants import ADDED, REMOVED, CHANGED1, CHANGED2, UNCHANGED


def dict_to_list(array: dict):
    result = []
    for key, value in array.items():
        if isinstance(value, dict):
            value = dict_to_list(value)
        result.append((UNCHANGED, key, value))
    return result

def walk(data_one: dict, data_two: dict):  # noqa: max-complexity: 10
    diff = []

    new_data_one = dict_to_list(data_one)
    new_data_two = dict_to_list(data_two)

    for suffix, key, value in new_data_one:
        if isinstance(value, list):
            if key in data_two and isinstance(data_two[key], dict):
                value = walk(data_one[key], data_two[key])
                new_data_two = [n for n in new_data_two if n[1] != key]
            elif key in data_two and isinstance(data_two[key], str):
                suffix = CHANGED1
            else:
                suffix = REMOVED
                value = dict_to_list(data_one[key])

            diff.append((suffix, key, value))
            continue
        if key in data_two and value == data_two[key]:
            new_data_two = [n for n in new_data_two if n[1] != key]

        elif key in data_two and value != data_two[key]:
            suffix = CHANGED1
        else:
            suffix = REMOVED
        diff.append((suffix, key, value))

    for suffix, key, value in new_data_two:
        if isinstance(value, list):
            value = walk(data_two[key], data_two[key])
        if key in data_one:
            suffix = CHANGED2
        else:
            suffix = ADDED
        diff.append((suffix, key, value))
    diff.sort(key=lambda x: x[1])
    return diff
