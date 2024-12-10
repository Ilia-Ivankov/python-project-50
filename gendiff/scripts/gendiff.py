#!/usr/bin/env python3
from gendiff.diff import generate_diff 
from gendiff.cli import get_args
import argparse


def main():
    args = get_args()
    diff = generate_diff(
        args.first_file, args.second_file, style=args.format
    )
    return diff


if __name__ == "__main__":
    main()
