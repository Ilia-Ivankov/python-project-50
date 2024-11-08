import argparse
from gendiff.generators.gendiff import generate_diff

def set_arguments():
    parser = argparse.ArgumentParser(add_help=True)
    parser = argparse.ArgumentParser(
        prog='gendiff', description='Compares two configuration files')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
