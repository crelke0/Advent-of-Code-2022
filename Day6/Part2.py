import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
for i in range(14, len(puzzle_input)):
  last_four = puzzle_input[i-14:i]
  if len(set(last_four)) == len(last_four):
    print(i)
    break