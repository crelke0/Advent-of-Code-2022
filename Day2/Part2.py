import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
puzzle_input = puzzle_input.split('\n')
score = 0
for line in puzzle_input:
  a, b = line.split(' ')
  a = 'ABC'.index(a)
  b = 'XYZ'.index(b)
  score += b*3 + (b + a + 2)%3 + 1
print(score)
