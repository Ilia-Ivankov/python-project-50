def checking_value(value):
    if isinstance(value, dict):
        result = "[complex value]"
    elif isinstance(value, bool):
        result = str(value).lower()
    elif isinstance(value, str):
        result = f"'{value}'"
    elif value is None:
        result = "null"
    else:
        result = str(value)
    return result


def to_plain(diff_tree):
    def _iter_plain(tree, path=""):
        result = []

        for node in tree:
            full_path = f"{path}.{node['key']}" if path else node["key"]
            node_type = node["type"]

            match node_type:
                case "removed":
                    result.append(f"Property '{full_path}' was removed")
                case "added":
                    value = checking_value(node["value"])
                    result.append(
                        f"Property '{full_path}' was added with value: {value}"
                    )
                case "changed":
                    old_value = checking_value(node["old_value"])
                    new_value = checking_value(node["new_value"])
                    result.append(
                        f"Property '{full_path}' was updated. From {old_value} "
                        f"to {new_value}"
                    )
                case "nested":
                    result.extend(_iter_plain(node["children"], full_path))

        return result

    return "\n".join(_iter_plain(diff_tree))
