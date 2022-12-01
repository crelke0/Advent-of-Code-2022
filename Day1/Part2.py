import os

def func(log):
  elves = []
  elf = 0
  for line in log:
    if line == '':
      elves.append(elf)
      elf = 0
    else:
      elf += int(line)
  
  elves = sorted(elves)
  return elves[-1] + elves[-2] + elves[-3]

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
print(func(puzzle_input.split("\n")))