from gendiff.formatters.helpers import format_value


def format_added(key, value, depth, symbol_indent):
    """Форматирует добавленные ключи."""
    return f"{symbol_indent}+ {key}: {format_value(value, depth)}"


def format_removed(key, value, depth, symbol_indent):
    """Форматирует удаленные ключи."""
    return f"{symbol_indent}- {key}: {format_value(value, depth)}"


def format_nested(key, value, depth, base_indent):
    """Форматирует вложенные ключи."""
    from gendiff.formatters.stylish import generate_diff
    nested_diff = generate_diff(
        file1=value[0],
        file2=value[1],
        depth=depth + 1
    )
    return f"{base_indent}{key}: {nested_diff}"


def process_key(key, data, depth):
    """Обрабатывает ключи и возвращает строки с форматированием в зависимости от различий."""
    file1, file2 = data["file1"], data["file2"]
    base_indent, symbol_indent = data["base_indent"], data["symbol_indent"]

    if key in file1 and key not in file2:
        return [format_removed(key, file1[key], depth, symbol_indent)]
    if key in file2 and key not in file1:
        return [format_added(key, file2[key], depth, symbol_indent)]
    if isinstance(file1[key], dict) and isinstance(file2[key], dict):
        nested_diff = format_nested(key, (file1[key], file2[key]), depth, base_indent)
        return [nested_diff]
    if file1[key] != file2[key]:
        return [
            format_removed(key, file1[key], depth, symbol_indent),
            format_added(key, file2[key], depth, symbol_indent),
        ]
    return [f"{base_indent}{key}: {format_value(file1[key], depth)}"]
