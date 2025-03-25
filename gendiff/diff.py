from gendiff.parser import read_file


def normalize_boolean(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2, format_name="plain"):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    data1 = {key: normalize_boolean(value) for key, value in data1.items()}
    data2 = {key: normalize_boolean(value) for key, value in data2.items()}
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_lines = []
    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff_lines.append(f"    {key}: {data1[key]}")
            else:
                diff_lines.append(f"  - {key}: {data1[key]}")
                diff_lines.append(f"  + {key}: {data2[key]}")
        elif key in data1:
            diff_lines.append(f"  - {key}: {data1[key]}")
        elif key in data2:
            diff_lines.append(f"  + {key}: {data2[key]}")

    return "{\n" + "\n".join(diff_lines) + "\n}"