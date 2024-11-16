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
            f'{nested_indent}{k}: {format_value(v, depth + 1)}'
            for k, v in value.items()
        ]
        return '{\n' + '\n'.join(formatted_items) + f'\n{closing_indent}}}'
    return str(value)


def generate_diff(file1, file2, depth=1, spaces_per_level=4):
    """Генерирует строку различий между двумя словарями с отступами."""
    diff = ['{']
    base_indent = ' ' * (depth * spaces_per_level)  # Базовый отступ
    symbol_indent = ' ' * (depth * spaces_per_level - 2)  # Отступ перед +/-

    all_keys = sorted(set(file1.keys()) | set(file2.keys()))  # Алфавитный порядок

    for key in all_keys:
        if key in file1 and key not in file2:
            diff.append(
                f'{symbol_indent}- {key}: {format_value(file1[key], depth)}'
            )
        elif key in file2 and key not in file1:
            diff.append(
                f'{symbol_indent}+ {key}: {format_value(file2[key], depth)}'
            )
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            nested_diff = generate_diff(file1[key], file2[key], depth + 1)
            diff.append(f'{base_indent}{key}: {nested_diff}')
        elif file1[key] != file2[key]:
            diff.append(
                f'{symbol_indent}- {key}: {format_value(file1[key], depth)}'
            )
            diff.append(
                f'{symbol_indent}+ {key}: {format_value(file2[key], depth)}'
            )
        else:
            diff.append(
                f'{base_indent}{key}: {format_value(file1[key], depth)}'
            )

    closing_indent = ' ' * ((depth - 1) * spaces_per_level)  # Отступ для закрытия
    diff.append(f'{closing_indent}}}')
    return '\n'.join(diff)
