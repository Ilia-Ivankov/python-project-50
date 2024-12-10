import json

import yaml


def read_json(file):
    return json.load(file)


def read_yaml(file):
    return yaml.safe_load(file)


def parse(file, extension):
    match extension:
        case "json":
            return read_json(file)
        case "yaml" | "yml":
            return read_yaml(file)
