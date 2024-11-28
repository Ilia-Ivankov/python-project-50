from gendiff.formatters.helpers import format_value_plain as format_value


def handle_removed(result, key, context):
    result.append(f"Property '{context['path']}' was removed")


def handle_added(result, key, context):
    result.append(
        f"Property '{context['path']}' was added with value: "
        f"{format_value(context['file2'][key], context['depth'])}"
    )


def handle_nested(result, key, context):
    result.extend(
        generate_diff(
            context['file1'][key], context['file2'][key], context['depth'] + 1, context['path']
        )
    )


def handle_updated(result, key, context):
    result.append(
        f"Property '{context['path']}' was updated. From "
        f"{format_value(context['file1'][key], context['depth'])} "
        f"to {format_value(context['file2'][key], context['depth'])}"
    )


def generate_diff(file1, file2, depth=1, path=""):
    result = []
    keys = sorted(set(file1.keys()) | set(file2.keys()))  # Упорядоченные ключи

    for key in keys:
        new_path = f"{path}.{key}" if path else key
        context = {
            "file1": file1,
            "file2": file2,
            "depth": depth,
            "path": new_path,
        }

        if key in file1 and key not in file2:
            handle_removed(result, key, context)
        elif key in file2 and key not in file1:
            handle_added(result, key, context)
        elif isinstance(file1.get(key), dict) and isinstance(file2.get(key), dict):
            handle_nested(result, key, context)
        elif file1.get(key) != file2.get(key):
            handle_updated(result, key, context)

    return result


def generate_plain_diff(file1, file2):
    result = generate_diff(file1, file2)
    return "\n".join(result)
