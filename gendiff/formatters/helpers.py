def format_value(value, depth, spaces_per_level=4):
    """Форматирует значение с учетом вложенности."""
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        nested_indent = ' ' * ((depth + 1) * spaces_per_level)
        closing_indent = ' ' * (depth * spaces_per_level)
        formatted_items = [
            f"{nested_indent}{k}: {format_value(v, depth + 1)}"
            for k, v in value.items()
        ]
        return "{\n" + "\n".join(formatted_items) + f"\n{closing_indent}}}"
    return str(value)
