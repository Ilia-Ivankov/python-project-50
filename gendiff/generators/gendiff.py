from gendiff.constants import TYPE_OF_DIFFERENCES
from gendiff.utils import read_json


def generate_diff(file1, file2):
  file1_dict = read_json(file1)
  file2_dict = read_json(file2)
  diff = []
  diff.append('{')
  for key in file1_dict:
    if key not in file2_dict:
      diff.append(f'  {TYPE_OF_DIFFERENCES["removed"]}{key}: {file1_dict[key]}')
    elif file1_dict[key] != file2_dict[key]:
      diff.append(f'  {TYPE_OF_DIFFERENCES["removed"]}{key}: {file1_dict[key]}')
      diff.append(f'  {TYPE_OF_DIFFERENCES["added"]}{key}: {file2_dict[key]}')
    else:
      diff.append(f'   {TYPE_OF_DIFFERENCES["unchanged"]}{key}: {file1_dict[key]}')
  for key in file2_dict:
    if key not in file1_dict:
      diff.append(f'  {TYPE_OF_DIFFERENCES["added"]}{key}: {file2_dict[key]}')
  diff.append('}')
  return '\n'.join(diff)
