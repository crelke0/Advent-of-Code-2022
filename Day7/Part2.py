import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
commands = puzzle_input.split('$ ')[1:]
CHILDS = 'childs'
DIRECT_SIZE = 'direct_size'
directory = {CHILDS: {'/': {CHILDS: {}, DIRECT_SIZE: 0}}}
current_path = []
current_folder = directory
for command in commands:
  if command[:2] == 'ls':
    lines = command.splitlines()[1:]
    for line in lines:
      if line[:3] != 'dir':
        current_folder[DIRECT_SIZE] += int(line.split(' ')[0])
  elif command[3]  == '.':
    current_path = current_path[:-1]
    folder = directory
    for next_folder in current_path:
      folder = folder[CHILDS][next_folder]
    current_folder = folder
  else:
    folder = command.split(' ')[1][:-1]
    if folder not in current_folder[CHILDS]:
      current_folder[CHILDS][folder] = {CHILDS: {}, DIRECT_SIZE: 0}
    current_folder = current_folder[CHILDS][folder]
    current_path.append(folder)

directory = directory[CHILDS]

sizes = []
def traverse(directory):
  global sizes
  total = directory[DIRECT_SIZE]
  for child in directory[CHILDS].values():
    total += traverse(child)
  sizes.append(total)
  return total

total = traverse(directory['/'])
space_needed = total - 40000000
smallest = None
for size in sizes:
  if space_needed < size and ((smallest == None) or (size < smallest)):
    smallest = size
print(smallest)
