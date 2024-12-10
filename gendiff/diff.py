import os

from gendiff.parser import parse
from gendiff.styles.json import to_json
from gendiff.styles.plain import to_plain
from gendiff.styles.stylish import to_stylish
from gendiff.tree import create_difference_tree


def get_extension(file_path):
    return os.path.splitext(file_path)[1][1:]


def get_file_data(file_path):
    with open(file_path) as file:
        return parse(file, get_extension(file_path))


def format_diff(diff_tree, style):
    if style == "stylish":
        return to_stylish(diff_tree)
    elif style == "plain":
        return to_plain(diff_tree)
    elif style == "json":
        return to_json(diff_tree)
    else:
        raise ValueError(f"Unsupported format: {style}")


def generate_diff(file1_path, file2_path, style="stylish"):
    data1 = get_file_data(file1_path)
    data2 = get_file_data(file2_path)
    diff_tree = create_difference_tree(data1, data2)
    return format_diff(diff_tree, style)
