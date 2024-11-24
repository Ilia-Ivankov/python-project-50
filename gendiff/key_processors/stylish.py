from gendiff.formatters.helpers import (
    format_value,
    format_added,
    format_removed,
    format_nested
)


def process_key_stylish(key, data):
    file1, file2 = data["file1"], data["file2"]
    depth = data["depth"]

    if key in file1 and key not in file2:
        return [format_removed(key, file1[key], depth)]
    elif key in file2 and key not in file1:
        return [format_added(key, file2[key], depth)]
    elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
        return format_nested(key, (file1[key], file2[key]), depth)
    elif file1[key] != file2[key]:
        return [
            format_removed(key, file1[key], depth),
            format_added(key, file2[key], depth),
        ]
    else:
        base_indent = " " * (depth * 4)
        return [f"{base_indent}{key}: {format_value(file1[key], depth)}"]
