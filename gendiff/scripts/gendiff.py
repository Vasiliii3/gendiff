#!/usr/bin/env python

import argparse
from gendiff import diff_files
from gendiff import __version__ as version

DESCRIPTION = 'Compares two configuration files and shows a difference.'

TYPE_FORMAT = ['stylish', ]


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument('first_file', type=str)

    parser.add_argument('second_file', type=str)

    parser.add_argument('--f', '--format', dest='format',
                        default="stylish", type=str,
                        choices=TYPE_FORMAT, metavar='[type]',
                        help='set format of output (default:stylish)')
    # увидел в видео, решил повторить, возможно и лишние
    parser.add_argument('--v', '--version', action='version', version=version)

    args = parser.parse_args()
    print(diff_files.generate_diff(args.first_file,
                                   args.second_file, args.format))


if __name__ == '__main__':
    main()
