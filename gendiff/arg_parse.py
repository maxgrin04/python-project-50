import argparse
from gendiff.diff import generate_diff


def arg_parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        type=str,
        help='set format of output (default: stylish)',
        default='stylish'
    )
    args = parser.parse_args()

    diff = generate_diff(
        args.first_file,
        args.second_file,
        format_name=args.format
    )
    print(diff)
