#!/usr/bin/env python

import argparse
from gendiff import diff_files


def main():

    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', type=str)

    parser.add_argument('second_file', type=str)

    parser.add_argument('--f', '--format', dest='FORMAT', help='set format of output')

    args = parser.parse_args()
    print(diff_files.generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
