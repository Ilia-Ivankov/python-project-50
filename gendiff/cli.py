import argparse
from gendiff import generate_diff
from gendiff.parser import parse_file


def set_arguments():
    parser = argparse.ArgumentParser(add_help=True)
    parser = argparse.ArgumentParser(
        prog='gendiff', description='Compares two configuration files')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_file = parse_file(args.first_file)
    second_file = parse_file(args.second_file)
    diff = generate_diff(first_file, second_file)
    print(diff)
