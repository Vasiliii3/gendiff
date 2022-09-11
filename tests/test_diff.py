from gendiff import diff_files
import pytest

file_json_1_flat = "tests/fixtures/file1.json"
file_json_2_flat = "tests/fixtures/file2.json"

file_json_3_tree = "tests/fixtures/file3.json"
file_json_4_tree = "tests/fixtures/file4.json"

file_yml_1_flat = 'tests/fixtures/file1.yml'
file_yml_2_flat = 'tests/fixtures/file2.yaml'

file_yml_3_tree = 'tests/fixtures/file3.yml'
file_yml_4_tree = 'tests/fixtures/file4.yml'

file_result_flat = "tests/fixtures/result_12_json.txt"
file_result_tree = "tests/fixtures/result_34_json(stylish).txt"
file_result_plain = "tests/fixtures/result_34_plain.txt"
file_result_json_json = "tests/fixtures/result_34_json(json).txt"

with open(file_result_flat, "r") as res:
    result_flat = res.read()

with open(file_result_tree, "r") as res:
    result_tree = res.read()

with open(file_result_plain, "r") as res:
    result_plain = res.read()

with open(file_result_json_json, "r") as res:
    result_json = res.read()


@pytest.mark.parametrize("file_one, file_two, file_result",
                         [
                             (file_json_1_flat, file_json_2_flat, result_flat),
                             (file_json_3_tree, file_json_4_tree, result_tree),
                             (file_yml_1_flat, file_yml_2_flat, result_flat),
                             (file_yml_3_tree, file_yml_4_tree, result_tree)
                         ])
def test_json_stylish(file_one, file_two, file_result):
    assert diff_files.generate_diff(file_one, file_two, "stylish") == file_result


def test_json_plain():
    assert diff_files.generate_diff(file_json_3_tree, file_json_4_tree, "plain") == result_plain


def test_json_json():
    assert diff_files.generate_diff(file_json_3_tree, file_json_4_tree, "json") == result_json


def test_empty():
    file1 = "tests/fixtures/file_empty.json"
    assert diff_files.generate_diff(file1, file1, "stylish") == '{\n}'
