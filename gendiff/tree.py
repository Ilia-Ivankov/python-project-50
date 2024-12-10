def create_difference_tree(data1, data2):
    """
    Создает дерево различий между двумя словарями.

    Args:
        data1 (dict): Первый словарь.
        data2 (dict): Второй словарь.

    Returns:
        dict: Дерево различий, содержащее информацию о добавленных, удаленных, измененных и неизмененных ключах.
    """
    keys = sorted(set(data1.keys()) | set(data2.keys()))  # Уникальные ключи из обоих словарей
    tree = []

    for key in keys:
        if key not in data1:
            tree.append({'key': key, 'type': 'added', 'value': data2[key]})
        elif key not in data2:
            tree.append({'key': key, 'type': 'removed', 'value': data1[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            # Рекурсивное сравнение для вложенных словарей
            tree.append({
                'key': key,
                'type': 'nested',
                'children': create_difference_tree(data1[key], data2[key])
            })
        elif data1[key] != data2[key]:
            tree.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
        else:
            tree.append({'key': key, 'type': 'unchanged', 'value': data1[key]})

    return tree
