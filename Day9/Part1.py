import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
instructions = puzzle_input.splitlines()
head = [0, 0]
head_previous = [0, 0]
tail = [0, 0]
visted = [[0, 0]]
def touching(head, tail):
  return 
for instruction in instructions:
  for n in range(int(instruction[2:])):
    head_previous = head.copy()
    head[0 if instruction[0] in 'LR' else 1] += -1 if instruction[0] in 'UL' else 1
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
      tail = head_previous
      if tail not in visted:
        visted.append(tail)

print(len(visted))
