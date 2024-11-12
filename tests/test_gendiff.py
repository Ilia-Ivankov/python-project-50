from gendiff.generators.gendiff import generate_diff
from gendiff.parser import parse_file

def test_gendiff():
    path_to_file1 = 'tests/fixtures/file1.json'
    path_to_file2 = 'tests/fixtures/file2.json'

    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    file1 = parse_file(path_to_file1)
    file2 = parse_file(path_to_file2)
    result = generate_diff(file1, file2)

    assert result == expected
