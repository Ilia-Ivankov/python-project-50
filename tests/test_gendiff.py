from gendiff.diff import generate_diff

def test_flt_json():
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
    file1 = path_to_file1
    file2 = path_to_file2
    result = generate_diff(file1, file2)

    assert result == expected


def test_flat_yaml():
    path_to_file1 = 'tests/fixtures/file1.yml'
    path_to_file2 = 'tests/fixtures/file2.yml'

    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    file1 = path_to_file1
    file2 = path_to_file2
    result = generate_diff(file1, file2)


def test_recursive_json():
    path_to_file1 = 'tests/fixtures/file3.json'
    path_to_file2 = 'tests/fixtures/file4.json'
    expected = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
    
    file1 = path_to_file1
    file2 = path_to_file2
    result = generate_diff(file1, file2)

    assert result == expected
