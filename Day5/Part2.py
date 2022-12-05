import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
# puzzle_input = '''    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2'''
stacks, instructions = puzzle_input.split('\n\n')
stacks = stacks.split('\n')
num_stacks = int(stacks[-1][-2])
stacks.pop()
stacks_list = [[] for _ in range(num_stacks)]
for i in range(len(stacks)):
  for j in range(num_stacks):
    box = stacks[i][j*4+1]
    if box != ' ':
      stacks_list[j].insert(0, box)

instructions = [line.split(',') for line in instructions.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split('\n')]
for line in instructions:
  amt = int(line[0])
  start = int(line[1]) - 1
  end = int(line[2]) - 1
  stacks_list[end] += stacks_list[start][-amt:]
  stacks_list[start] = stacks_list[start][:-amt]
print(''.join([stack[-1] for stack in stacks_list]))