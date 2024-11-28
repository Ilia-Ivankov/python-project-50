import json
from gendiff.key_processors.json import process_key_json


def generate_diff(file1, file2, depth=1):
    keys = sorted(set(file1.keys()) | set(file2.keys()))
    diff = []

    for key in keys:
        data = {
            "file1": file1,
            "file2": file2,
            "depth": depth,
        }
        key_diff = process_key_json(key, data)

        diff.append(key_diff)

    return diff


def generate_json_diff(file1, file2):
    diff = generate_diff(file1, file2)
    return json.dumps(diff, indent=4)
