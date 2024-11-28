from gendiff.formatters.stylish import generate_stylish_diff
from gendiff.parser import parse_file
from gendiff.formatters.plain import generate_plain_diff
from gendiff.formatters.json import generate_json_diff


def generate_diff(file1_path, file2_path, format_name="stylish"):
    """
    Generates a diff representation between two files in the specified format.

    Args:
        file1_path (str): The path to the first file.
        file2_path (str): The path to the second file.
        format_name (str): The name of the desired format ("stylish", "plain").

    Returns:
        str: A string representing the differences in the specified format.

    Raises:
        ValueError: If the provided format_name is not supported.
    """
    # Parse the input files using parse_file
    file1 = parse_file(file1_path)
    file2 = parse_file(file2_path)

    if format_name == "stylish":
        return generate_stylish_diff(file1, file2)
    if format_name == "plain":
        return generate_plain_diff(file1, file2)
    if format_name == "json":
        return generate_json_diff(file1, file2)
    else:
        raise ValueError(f"Unsupported format: {format_name}")
