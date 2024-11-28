def process_key_json(key, data):
    file1, file2 = data["file1"], data["file2"]
    depth = data["depth"]
    result = {"key": key}

    if key in file1 and key not in file2:
        result.update(handle_removed(key, file1[key]))
    elif key in file2 and key not in file1:
        result.update(handle_added(key, file2[key]))
    elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
        result.update(handle_nested(key, file1[key], file2[key], depth))
    elif file1[key] != file2[key]:
        result.update(handle_updated(key, file1[key], file2[key]))
    else:
        result.update(handle_unchanged(key, file1[key]))

    return result


def handle_added(key, value):
    return {"status": "added", "value": value}


def handle_removed(key, value):
    return {"status": "removed", "value": value}


def handle_updated(key, value1, value2):
    return {
        "status": "updated",
        "old_value": value1,
        "new_value": value2,
    }


def handle_unchanged(key, value):
    return {"status": "unchanged", "value": value}


def handle_nested(key, file1_value, file2_value, depth):
    from gendiff.formatters.json import generate_diff

    children = generate_diff(file1_value, file2_value, depth + 1)
    return {"status": "nested", "children": children}
