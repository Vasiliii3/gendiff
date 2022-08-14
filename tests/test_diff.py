from gendiff import diff_files


file_path1 = "tests/fixtures/file1.json"
file_path2 = "tests/fixtures/file2.json"
file_result = "tests/fixtures/result_1_json"

with open(file_result, "r") as res:
    result = res.read()


def test_json_plan():
    assert diff_files.generate_diff(file_path1, file_path2) == result
