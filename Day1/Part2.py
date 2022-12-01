import os

def func(lines):
  n = 3
  bests = [0]*n
  total = 0
  for line in lines:
    if line == '':
      for i in range(0, n - 1):
        if total > bests[i]:
          bests.insert(i, total)
          bests = bests[:n]
          break
      total = 0
    else:
      total += int(line)
  return sum(bests)

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
print(func(puzzle_input.split("\n")))
