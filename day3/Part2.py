import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
lines = puzzle_input.split('\n')
total = 0
for i in range(0, len(lines), 3):
  common = set(lines[i]).intersection(lines[i + 1]).intersection(lines[i + 2]).pop()
  order = ord(common)
  priority = order - (38 if 64 < order < 91 else 96)
  total += priority
print(total)
