def dict_to_list(array):
    result = []
    for key, value in array.items():
        if isinstance(value, dict):
            value = dict_to_list(value)
        result.append((" ", key, value))
    return result

def walk(dict1, dict2): # noqa: max-complexity: 10
    result = []

    list1 = dict_to_list(dict1)
    list2 = dict_to_list(dict2)

    for suffix, key, value in list1:
        if isinstance(value, list):
            if key in dict2 and isinstance(dict2[key], dict):
                value = walk(dict1[key], dict2[key])
                list2 = [n for n in list2 if n[1] != key]
            else:
                value = dict_to_list(dict1[key])
                suffix = "-"

            result.append((suffix, key, value))
            continue
        if key in dict2 and value == dict2[key]:
            list2 = [n for n in list2 if n[1] != key]
        else:
            suffix = "-"
        result.append((suffix, key, value))

    for suffix, key, value in list2:
        if isinstance(value, list):
            value = walk(dict2[key], dict2[key])
        result.append(("+", key, value))
    result.sort(key=lambda x: x[1])
    return result
