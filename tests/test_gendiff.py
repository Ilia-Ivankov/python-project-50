from gendiff.diff import generate_diff

from tests.expectations.json import expectation1 as json_expectation

from tests.expectations.plain import expectation1 as plain_expectation

from tests.expectations.stylish import expectation1, expectation2


def test_flat_json():
    path_to_file1 = "tests/fixtures/file1.json"
    path_to_file2 = "tests/fixtures/file2.json"
    file1 = path_to_file1
    file2 = path_to_file2
    result = generate_diff(file1, file2)

    assert result == expectation1


def test_flat_yaml():
    path_to_file1 = "tests/fixtures/file1.yml"
    path_to_file2 = "tests/fixtures/file2.yml"
    file1 = path_to_file1
    file2 = path_to_file2
    result = generate_diff(file1, file2)

    assert result == expectation1


def test_recursive_json():
    path_to_file1 = "tests/fixtures/file3.json"
    path_to_file2 = "tests/fixtures/file4.json"
    file1 = path_to_file1
    file2 = path_to_file2
    result = generate_diff(file1, file2)

    assert result == expectation2


def test_recusive_yaml():
    path_to_file1 = "tests/fixtures/file5.yml"
    path_to_file2 = "tests/fixtures/file6.yml"
    file1 = path_to_file1
    file2 = path_to_file2
    result = generate_diff(file1, file2)

    assert result == expectation2


def test_plain_json():
    path_to_file1 = "tests/fixtures/file3.json"
    path_to_file2 = "tests/fixtures/file4.json"
    file1 = path_to_file1
    file2 = path_to_file2
    result = generate_diff(file1, file2, format_name="plain")

    assert result == plain_expectation


def test_plain_yaml():
    path_to_file1 = "tests/fixtures/file5.yml"
    path_to_file2 = "tests/fixtures/file6.yml"
    file1 = path_to_file1
    file2 = path_to_file2
    result = generate_diff(file1, file2, format_name="plain")

    assert result == plain_expectation


def test_json():
    path_to_file1 = "tests/fixtures/file3.json"
    path_to_file2 = "tests/fixtures/file4.json"
    file1 = path_to_file1
    file2 = path_to_file2
    result = generate_diff(file1, file2, format_name="json")

    assert result == json_expectation


def test_json_yaml():
    path_to_file1 = "tests/fixtures/file5.yml"
    path_to_file2 = "tests/fixtures/file6.yml"
    file1 = path_to_file1
    file2 = path_to_file2
    result = generate_diff(file1, file2, format_name="json")

    assert result == json_expectation
