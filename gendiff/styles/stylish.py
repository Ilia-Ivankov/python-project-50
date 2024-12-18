def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        indent = build_indent(depth + 1)
        closing_indent = build_indent(depth)
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
        return "{\n" + "\n".join(lines) + f"\n{closing_indent}}}"
    elif value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    return str(value)


def build_indent(depth, offset=0):
    return "    " * (depth + offset)


def generate_stylish_diff(tree, depth=1):
    result = []

    for node in tree:
        key = node["key"]

        match node["type"]:
            case "added":
                result.append(
                    f"{build_indent(depth - 1)}  + {key}: "
                    f"{format_value(node['value'], depth)}"
                )
            case "removed":
                result.append(
                    f"{build_indent(depth - 1)}  - {key}: "
                    f"{format_value(node['value'], depth)}"
                )
            case "changed":
                result.append(
                    f"{build_indent(depth - 1)}  - {key}: "
                    f"{format_value(node['old_value'], depth)}"
                )
                result.append(
                    f"{build_indent(depth - 1)}  + {key}: "
                    f"{format_value(node['new_value'], depth)}"
                )
            case "nested":
                nested_data = generate_stylish_diff(node["children"], depth + 1)
                result.append(
                    f"{build_indent(depth - 1)}    {key}: {{\n{nested_data}\n"
                    f"{build_indent(depth)}}}"
                )
            case "unchanged":
                result.append(
                    f"{build_indent(depth - 1)}    {key}: "
                    f"{format_value(node['value'], depth)}"
                )

    return "\n".join(result)


def to_stylish(tree):
    return f"{{\n{generate_stylish_diff(tree)}\n}}"
