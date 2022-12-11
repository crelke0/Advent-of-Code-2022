import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
lines = puzzle_input.splitlines()
x_reg = 1
line_index = 0
add = 0
executing_stage = 0
for cycle in range(1, 241):
  line = lines[line_index]
  if executing_stage == 0:
    line_index = line_index + 1
    x_reg += add
    if line[:4] =='addx':
      executing_stage = 2
      add = int(line.split(' ')[1])
    else:
      add = 0
  executing_stage = max(0, executing_stage - 1)

  x_pos = (cycle - 1)%40
  if x_pos == 0:
    print()
  if abs(x_reg - x_pos) <= 1:
    print('#', end='')
  else:
    print('.', end='')
