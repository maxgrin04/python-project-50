from gendiff.diff import generate_diff
import pytest


@pytest.mark.parametrize("file_path1, file_path2, expected, format_name", [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'tests/fixtures/expected_result_1.txt', 'plain')
])
def test_generate_diff(file_path1, file_path2, expected, format_name):
    with open(expected, 'r') as file:
        expected_result = file.read()
    diff = generate_diff(file_path1, file_path2, format_name)
    assert diff == expected_result