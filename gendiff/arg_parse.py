import argparse
from gendiff.diff import generate_diff

def arg_parse():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        default="plain"  
    )
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, format_name=args.format)
    print(diff)
