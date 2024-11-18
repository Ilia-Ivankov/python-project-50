from gendiff.key_processor import process_key


def generate_diff(file1, file2, depth=1, spaces_per_level=4):
    diff = ["{"]
    data = {
        "file1": file1,
        "file2": file2,
        "base_indent": " " * (depth * spaces_per_level),
        "symbol_indent": " " * (depth * spaces_per_level - 2),
    }
    all_keys = sorted(set(file1.keys()) | set(file2.keys()))
    for key in all_keys:
        diff.extend(process_key(key, data, depth))
    diff.append(" " * ((depth - 1) * spaces_per_level) + "}")
    return "\n".join(diff)
