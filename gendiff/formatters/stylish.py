from gendiff.key_processors.stylish import process_key_stylish


def generate_stylish_diff(file1, file2, depth=1):
    result = []
    keys = sorted(set(file1.keys()) | set(file2.keys()))

    for key in keys:
        data = {
            "file1": file1,
            "file2": file2,
            "key": key,
            "depth": depth,
        }
        result.extend(
            process_key_stylish(key, data)
        )

    indent = " " * ((depth - 1) * 4)
    return "{\n" + "\n".join(result) + f"\n{indent}}}"
