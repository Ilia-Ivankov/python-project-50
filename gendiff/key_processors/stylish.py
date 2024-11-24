from gendiff.formatters.helpers import (
    format_value,
    format_added,
    format_removed,
    format_nested
)


def handle_removed(result, key, file1, depth):
    """Обрабатывает удаленные ключи."""
    result.append(format_removed(key, file1[key], depth))


def handle_added(result, key, file2, depth):
    """Обрабатывает добавленные ключи."""
    result.append(format_added(key, file2[key], depth))


def handle_updated(result, key, file1, file2, depth):
    """Обрабатывает измененные ключи."""
    result.append(
        format_removed(key, file1[key], depth),
    )
    result.append(
        format_added(key, file2[key], depth),
    )


def handle_unchanged(result, key, file1, depth):
    """Обрабатывает неизмененные ключи."""
    base_indent = " " * (depth * 4)
    result.append(f"{base_indent}{key}: {format_value(file1[key], depth)}")


def process_key_stylish(key, data):
    file1, file2 = data["file1"], data["file2"]
    depth = data["depth"]
    result = []

    # Обработка добавленных и удаленных значений
    if key in file1 and key not in file2:
        handle_removed(result, key, file1, depth)
    elif key in file2 and key not in file1:
        handle_added(result, key, file2, depth)
    # Обработка вложенных объектов
    elif isinstance(file1.get(key), dict) and isinstance(file2.get(key), dict):
        result.extend(format_nested(key, (file1[key], file2[key]), depth))
    # Обработка измененных значений
    elif file1.get(key) != file2.get(key):
        handle_updated(result, key, file1, file2, depth)
    # Обработка неизмененных значений
    else:
        handle_unchanged(result, key, file1, depth)

    return result
