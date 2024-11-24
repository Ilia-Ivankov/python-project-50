from gendiff.helpers import handle_added, handle_removed
from gendiff.helpers import handle_nested, handle_unchanged


def process_key_stylish(key, data):
    """Process a single key for the stylish diff."""
    file1, file2 = data["file1"], data["file2"]
    depth = data["depth"]
    base_indent = " " * (depth * 4)
    symbol_indent = " " * (depth * 4 - 2)

    if key in file1 and key not in file2:
        return [handle_removed(key, file1[key], symbol_indent, depth)]
    if key in file2 and key not in file1:
        return [handle_added(key, file2[key], symbol_indent, depth)]
    if isinstance(file1[key], dict) and isinstance(file2[key], dict):
        return [handle_nested(key, file1[key], file2[key], base_indent, depth)]
    if file1[key] != file2[key]:
        return [
            handle_removed(key, file1[key], symbol_indent, depth),
            handle_added(key, file2[key], symbol_indent, depth),
        ]
    return [handle_unchanged(key, file1[key], base_indent, depth)]
