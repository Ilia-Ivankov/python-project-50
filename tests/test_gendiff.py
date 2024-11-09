from gendiff.generators.gendiff import generate_diff

def test_gendiff():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'

    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

    result = generate_diff(file1, file2)

    assert result == expected
