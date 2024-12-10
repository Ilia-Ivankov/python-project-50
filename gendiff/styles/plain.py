def checking_value(value):
    """
    Преобразует значение для отображения в формате plain.

    Args:
        value: Значение любого типа.

    Returns:
        str: Преобразованное значение.
    """
    if isinstance(value, (bool, int)):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, dict):
        return f'[complex value]'
    return str(value)


def to_plain(diff_tree):
    """
    Преобразует дерево различий в плоский формат.

    Args:
        diff_tree (list): Дерево различий.

    Returns:
        str: Форматированная строка.
    """
    def _iter_plain(tree, path=""):
        result = []

        for node in tree:
            full_path = f"{path}.{node['key']}" if path else node['key']
            node_type = node['type']

            match node_type:
                case "removed":
                    result.append(f"Property '{full_path}' was removed")
                case "added":
                    value = checking_value(node['value'])
                    result.append(f"Property '{full_path}' was added with value: {checking_value(value)}")
                case "changed":
                    old_value = checking_value(node['old_value'])
                    new_value = checking_value(node['new_value'])
                    result.append(
                        f"Property '{full_path}' was updated. From {checking_value(old_value)} to {checking_value(new_value)}"
                    )
                case "nested":
                    result.extend(_iter_plain(node['children'], full_path))

        return result

    return "\n".join(_iter_plain(diff_tree))
