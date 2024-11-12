from gendiff.constants import TYPE_OF_DIFFERENCES


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file1, file2):
    diff = ['{']

    for key in sorted(file1):
        if key not in file2:
            diff.append(
                f'  {TYPE_OF_DIFFERENCES["removed"]}{key}: {format_value(file1[key])}'
            )
        elif file1[key] != file2[key]:
            diff.append(
                f'  {TYPE_OF_DIFFERENCES["removed"]}{key}: {format_value(file1[key])}'
            )
            diff.append(
                f'  {TYPE_OF_DIFFERENCES["added"]}{key}: {format_value(file2[key])}'
            )
        else:
            diff.append(
                f'   {TYPE_OF_DIFFERENCES["unchanged"]}{key}: {format_value(file1[key])}'
            )

    for key in sorted(file2):
        if key not in file1:
            diff.append(
                f'  {TYPE_OF_DIFFERENCES["added"]}{key}: {format_value(file2[key])}'
            )

    diff.append('}')
    return '\n'.join(diff)
