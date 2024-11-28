from gendiff.formatters.helpers import format_value_plain as format_value


def handle_removed(result, key, path):
    result.append(f"Property '{path}' was removed")


def handle_added(result, key, path, file2, depth):
    result.append(
        f"Property '{path}' was added with value: {format_value(file2[key], depth)}"
    )


def handle_nested(result, key, file1, file2, depth, path):
    result.extend(generate_diff(file1[key], file2[key], depth + 1, path))


def handle_updated(result, key, path, file1, file2, depth):
    result.append(
        f"Property '{path}' was updated. From {format_value(file1[key], depth)} "
        f"to {format_value(file2[key], depth)}"
    )


def generate_diff(file1, file2, depth=1, path=""):
    result = []
    keys = sorted(set(file1.keys()) | set(file2.keys()))  # Объединение ключей

    for key in keys:
        new_path = f"{path}.{key}" if path else key
        if key in file1 and key not in file2:
            handle_removed(result, key, new_path)
        elif key in file2 and key not in file1:
            handle_added(result, key, new_path, file2, depth)
        elif isinstance(file1.get(key), dict) and isinstance(file2.get(key), dict):
            handle_nested(result, key, file1, file2, depth, new_path)
        elif file1.get(key) != file2.get(key):
            handle_updated(result, key, new_path, file1, file2, depth)

    return result


def generate_plain_diff(file1, file2):
    result = generate_diff(file1, file2)
    return "\n".join(result)
