import argparse
import json

def arg_parse():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        default="plain"  # Формат по умолчанию
    )
    args = parser.parse_args()

    # Выводим переданные аргументы
    print(f"Comparing {args.first_file} and {args.second_file} in {args.format} format.")

    json.load(open('gendiff/file1.json'))