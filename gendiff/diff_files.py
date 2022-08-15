from .parsing import open_file
from gendiff.style import style_stylih

DICT_REPLACEMENT = {False: "false",
                    True: "true",
                    None: "null"
                    }


def dict_to_list(array: dict) -> list:
    list_temp = []
    for key, value in array.items():
        list_temp.append((key, DICT_REPLACEMENT.get(value, value)))
    list_temp.sort(key=lambda x: x[0])
    return list_temp


def delet_valus_list(array, val):
    return [n for n in array if n[0] != val]


def generate_diff(file_path1, file_path2):
    dict1 = open_file(file_path1)
    dict2 = open_file(file_path2)

    list1 = dict_to_list(dict1)
    list2 = dict_to_list(dict2)

    list_temp = []

    for key, value in list1:
        if key in dict2 and value == dict2[key]:
            list_temp.append((" ", key, value))
            list2 = delet_valus_list(list2, key)
        else:
            list_temp.append(("-", key, value))

    for key, value in list2:
        list_temp.append(("+", key, value))

    result = style_stylih(list_temp)
    return result
