import json
INDENT = 4


def styling_json(tree: list) -> str:
    def walk(tree_: list):
        json_dict = dict()
        for nodes in tree_:
            diff, key, value = nodes
            if isinstance(value, list):
                value = walk(value)
            json_dict[f'{diff} {key}'] = value
        return json_dict

    return json.dumps(walk(tree), indent=INDENT)
