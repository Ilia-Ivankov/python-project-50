from gendiff.formatters.helpers import (
    format_added,
    format_nested,
    format_removed,
    format_value,
)


def handle_removed(key, file1, depth):
    """Обрабатывает удаленные ключи."""
    return format_removed(key, file1[key], depth)


def handle_added(key, file2, depth):
    """Обрабатывает добавленные ключи."""
    return format_added(key, file2[key], depth)


def handle_updated(key, file1, file2, depth):
    """Обрабатывает измененные ключи."""
    return [
        format_removed(key, file1[key], depth),
        format_added(key, file2[key], depth),
    ]


def handle_unchanged(key, file1, depth):
    """Обрабатывает неизмененные ключи."""
    base_indent = " " * (depth * 4)
    return [f"{base_indent}{key}: {format_value(file1[key], depth)}"]


def process_key_stylish(key, data):
    file1, file2 = data["file1"], data["file2"]
    depth = data["depth"]
    result = []

    if key in file1 and key not in file2:
        result.append(handle_removed(key, file1, depth))
    elif key in file2 and key not in file1:
        result.append(handle_added(key, file2, depth))
    elif isinstance(file1.get(key), dict) and isinstance(file2.get(key), dict):
        result.extend(format_nested(key, (file1[key], file2[key]), depth))
    elif file1.get(key) != file2.get(key):
        result.extend(handle_updated(key, file1, file2, depth))
    else:
        result.extend(handle_unchanged(key, file1, depth))

    return result
