import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
lines = puzzle_input.split('\n')
total = 0
for line in lines:
  elves = line.split(',')
  elf_1 = elves[0].split('-')
  elf_2 = elves[1].split('-')
  min_1, max_1 = int(elf_1[0]), int(elf_1[1])
  min_2, max_2 = int(elf_2[0]), int(elf_2[1])
  if min_1 >= min_2 and max_1 <= max_2:
    total += 1
  elif min_1 <= min_2 and max_1 >= max_2:
    total += 1
print(total)
