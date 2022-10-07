from gendiff import diff_files
import pytest
import os


def get_fixture_path(name):
    return os.path.join('tests', 'fixtures', name)


file_json_1_flat = get_fixture_path('file1.json')
file_json_2_flat = get_fixture_path('file2.json')

file_json_3_tree = get_fixture_path('file3.json')
file_json_4_tree = get_fixture_path('file4.json')

file_yml_1_flat = get_fixture_path('file1.yml')
file_yml_2_flat = get_fixture_path('file2.yaml')

file_yml_3_tree = get_fixture_path('file3.yml')
file_yml_4_tree = get_fixture_path('file4.yml')

file_result_flat = get_fixture_path('result_12_json.txt')
file_result_tree = get_fixture_path('result_34_json(stylish).txt')
file_result_plain = get_fixture_path('result_34_plain.txt')
file_result_json_json = get_fixture_path('result_34_json(json).txt')


def open_file(file):
    with open(file, "r") as res:
        result = res.read()
    return result


@pytest.fixture
def result_flat():
    return open_file(file_result_flat)


@pytest.fixture
def result_tree():
    return open_file(file_result_tree)


@pytest.fixture
def result_plain():
    return open_file(file_result_plain)


@pytest.fixture
def result_json():
    return open_file(file_result_json_json)


@pytest.mark.parametrize("file_one, file_two",
                         [
                             (file_json_1_flat, file_json_2_flat),
                             (file_yml_1_flat, file_yml_2_flat),
                         ])
def test_flat_stylish(file_one, file_two, result_flat):
    assert diff_files.generate_diff(file_one, file_two) == result_flat


@pytest.mark.parametrize("file_one, file_two",
                         [
                             (file_json_3_tree, file_json_4_tree),
                             (file_yml_3_tree, file_yml_4_tree)
                         ])
def test_tree_stylish(file_one, file_two, result_tree):
    assert diff_files.generate_diff(file_one, file_two) == result_tree


def test_json_plain(result_plain):
    assert diff_files.generate_diff(file_json_3_tree, file_json_4_tree, "plain") == result_plain


def test_json_json(result_json):
    assert diff_files.generate_diff(file_json_3_tree, file_json_4_tree, "json") == result_json


def test_empty():
    file1 = get_fixture_path('file_empty.json')
    assert diff_files.generate_diff(file1, file1, "stylish") == '{\n}'