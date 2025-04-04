from formatters.stylish import format_stylish
from formatters.plain import format_plain
from formatters.json import format_json


def get_formatter(formatter_name):
    match formatter_name:
        case 'stylish':
            return format_stylish
        case 'plain':
            return format_plain
        case 'json':
            return format_json
        case _:
            raise ValueError(f"Unsupported formatter: {formatter_name}")