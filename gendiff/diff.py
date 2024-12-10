import os
from gendiff.parser import parse
from gendiff.tree import create_difference_tree  # Функция для создания дерева различий
from gendiff.styles.stylish import to_stylish
from gendiff.styles.plain import to_plain
from gendiff.styles.json import generate_json_diff

def get_extension(file_path):
    """
    Получить расширение файла из его пути.

    Args:
        file_path (str): Путь к файлу.

    Returns:
        str: Расширение файла (без точки).
    """
    return os.path.splitext(file_path)[1][1:]

def get_file_data(file_path):
    """
    Прочитать и распарсить данные из файла.

    Args:
        file_path (str): Путь к файлу.

    Returns:
        dict: Распарсенные данные из файла.
    """
    with open(file_path) as file:
        return parse(file, get_extension(file_path))

def format_diff(diff_tree, style):
    """
    Отформатировать дерево различий в указанном стиле.

    Args:
        diff_tree (dict): Дерево различий.
        style (str): Формат вывода ("stylish", "plain", "json").

    Returns:
        str: Отформатированная строка различий.

    Raises:
        ValueError: Если указанный стиль не поддерживается.
    """
    if style == "stylish":
        return to_stylish(diff_tree)  # Возвращаем результат
    elif style == "plain":
        return to_plain(diff_tree)
    elif style == "json":
        return generate_json_diff(diff_tree)
    else:
        raise ValueError(f"Unsupported format: {style}")

def generate_diff(file1_path, file2_path, style="stylish"):
    """
    Генерация различий между двумя файлами в указанном формате.

    Args:
        file1_path (str): Путь к первому файлу.
        file2_path (str): Путь ко второму файлу.
        style (str): Формат вывода ("stylish", "plain", "json").

    Returns:
        str: Строка с различиями в заданном формате.
    """
    data1 = get_file_data(file1_path)
    data2 = get_file_data(file2_path)
    diff_tree = create_difference_tree(data1, data2)
    print("Generated diff tree:", diff_tree)  # Отладочный вывод
    return format_diff(diff_tree, style)
