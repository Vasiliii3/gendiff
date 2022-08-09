def style_stylih(array: list)-> str:
    level = 1
    result = f'{{\n'
    for string in array:
        diff, key, value = string
        emtpy = " " * level
        result += f'{emtpy} {diff} {key}: {value}\n'
    result += "}"
    return result

