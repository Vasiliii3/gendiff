from gendiff import diff_files
import pytest

file_json_one_flat = "tests/fixtures/file1.json"
file_json_two_flat = "tests/fixtures/file2.json"

file_yml_one_flat = 'tests/fixtures/file1.yml'
file_yml_two_flat = 'tests/fixtures/file2.yaml'

file_result_flat = "tests/fixtures/result_1_json"

with open(file_result_flat, "r") as res:
    result_flat = res.read()


@pytest.mark.parametrize("file_one, file_two, file_result",
                         [
                             (file_json_one_flat, file_json_two_flat, result_flat),
                             (file_yml_one_flat, file_yml_two_flat, result_flat)
                         ])
def test_json_plan(file_one, file_two, file_result):
    assert diff_files.generate_diff(file_one, file_two) == file_result
