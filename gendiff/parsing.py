import json
import yaml

PARSERS = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "yml": yaml.safe_load,
}


def parse(data, type_file):
    return PARSERS[type_file](data)
