import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()

commands = puzzle_input.split('$ ')[1:]
path = []
sizes = {}
for command in commands:
  if command[:2] == 'ls':
    lines = command.splitlines()[1:]
    direct_size = 0
    for line in lines:
      if line[:3] != 'dir':
        direct_size += int(line.split(' ')[0])
    sizes[''.join(path)] = direct_size

    for i in range(1, len(path)):
      sizes[''.join(path[:i])] += direct_size
      
  elif command[3:5] == '..':
    path.pop()
  else:
    folder = command[3:-1]
    path.append(folder)
    sizes[''.join(path)] = 0

space_needed = sizes['/'] - 40000000
smallest = float('inf')
for size in sizes.values():
  if smallest > size > space_needed:
    smallest = size

print(smallest)
