def format_value(value, depth, spaces_per_level=4):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        nested_indent = " " * ((depth + 1) * spaces_per_level)
        closing_indent = " " * (depth * spaces_per_level)
        formatted_items = [
            f"{nested_indent}{k}: {format_value(v, depth + 1)}"
            for k, v in value.items()
        ]
        return "{\n" + "\n".join(formatted_items) + f"\n{closing_indent}}}"
    return str(value)


def format_added(key, value, depth):
    indent = " " * (depth * 4 - 2)  # Отступ для символа "+"
    return f"{indent}+ {key}: {format_value(value, depth)}"


def format_removed(key, value, depth):
    indent = " " * (depth * 4 - 2)  # Отступ для символа "-"
    return f"{indent}- {key}: {format_value(value, depth)}"


def format_nested(key, values, depth):
    from gendiff.formatters.stylish import generate_stylish_diff

    file1_value, file2_value = values
    nested_diff = generate_stylish_diff(file1_value, file2_value, depth + 1)
    nested_indent = " " * (depth * 4)

    return [f"{nested_indent}{key}: {nested_diff}"]


def format_value_plain(value, depth):
    if isinstance(value, dict):
        result = "[complex value]"
    elif isinstance(value, bool):
        result = str(value).lower()
    elif isinstance(value, str):
        result = f"'{value}'"
    elif value is None:
        result = "null"
    else:
        result = str(value)
    return result
