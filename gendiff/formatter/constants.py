def to_str_python_to_json(value):
    if value is False:
        return "false"
    elif value is True:
        return "true"
    elif value is None:
        return "null"
    return value


TYPE_FORMAT = ['stylish', 'plain', 'json']
TYPE_FILE = ["json", "yml", "yaml"]
