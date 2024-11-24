def format_value(value, depth):
    # Если значение является словарем, то это сложное значение
    if isinstance(value, dict):
        return "[complex value]"
    # Если значение - булево, то выводим его в нижнем регистре
    elif isinstance(value, bool):
        return str(value).lower()
    # Если строка, то оборачиваем в одинарные кавычки
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)  # Для других типов данных, возвращаем строковое представление


def generate_diff(file1, file2, depth=1, path=""):
    result = []
    keys = sorted(set(file1.keys()) | set(file2.keys()))  # Объединение ключей

    for key in keys:
        new_path = f"{path}.{key}" if path else key
        if key in file1 and key not in file2:
            result.append(f"Property '{new_path}' was removed")
        elif key in file2 and key not in file1:
            result.append(
                f"Property '{new_path}' was added with value: {format_value(file2[key], depth)}"
            )
        elif isinstance(file1.get(key), dict) and isinstance(file2.get(key), dict):
            # Рекурсивно обрабатываем вложенные объекты
            result.extend(generate_diff(file1[key], file2[key], depth + 1, new_path))
        elif file1.get(key) != file2.get(key):
            result.append(
                f"Property '{new_path}' was updated. From {format_value(file1[key], depth)} "
                f"to {format_value(file2[key], depth)}"
            )

    return result  # Возвращаем результат как строку


def generate_plain_diff(file1, file2):
    result = generate_diff(file1, file2)
    return "\n".join(result)
