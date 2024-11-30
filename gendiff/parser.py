from gendiff.utils import read_json, read_yaml


def parse_file(file):
    if file.endswith((".yaml", ".yml")):
        return read_yaml(file)
    elif file.endswith(".json"):
        return read_json(file)
