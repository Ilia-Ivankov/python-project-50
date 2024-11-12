import json
import yaml


def read_json(file):
    return json.load(open(file))


def read_yaml(file):
    return yaml.safe_load(open(file))
