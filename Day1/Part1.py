import os

def func(lines):
  largest = 0
  total = 0
  for line in lines:
    if line == '':
      if total > largest:
        largest = total
      total = 0
    else:
      total += int(line
  
  return largest

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
print(func(puzzle_input.split("\n")))
