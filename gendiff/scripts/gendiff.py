#!/usr/bin/env python

import argparse


def main():

    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', type=str)

    parser.add_argument('second_file', type=str)

    parser.add_argument('--f', '--format', dest='FORMAT', help='set format of output')

    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
