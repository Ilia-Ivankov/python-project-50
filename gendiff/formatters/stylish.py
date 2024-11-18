from gendiff.key_processor import process_key


def generate_diff(file1, file2, depth=1, spaces_per_level=4):
    diff = ['{']
    base_indent = ' ' * (depth * spaces_per_level)
    symbol_indent = ' ' * (depth * spaces_per_level - 2)

    # Получаем все ключи из обоих файлов в алфавитном порядке
    all_keys = sorted(set(file1.keys()) | set(file2.keys()))

    for key in all_keys:
        diff.extend(process_key(key, file1, file2, depth, base_indent, symbol_indent))

    # Отступ для закрытия фигурной скобки
    closing_indent = ' ' * ((depth - 1) * spaces_per_level)
    diff.append(f'{closing_indent}}}')
    return '\n'.join(diff)
