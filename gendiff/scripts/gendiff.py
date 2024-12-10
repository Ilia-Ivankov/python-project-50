#!/usr/bin/env python3

from gendiff.cli import get_args
from gendiff.diff import generate_diff


def main():
    args = get_args()
    diff = generate_diff(args.first_file, args.second_file, style=args.format)
    return diff


if __name__ == "__main__":
    print(main())
