import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
for i in range(4, len(puzzle_input)):
  last_four = puzzle_input[i-4:i]
  if len(set(last_four)) == len(last_four):
    print(i)
    break