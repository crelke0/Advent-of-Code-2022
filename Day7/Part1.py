import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()

commands = puzzle_input.split('$ ')[1:]
path = []
sizes = {}
total = 0
for command in commands:
  if command[:2] == 'ls':
    lines = command.splitlines()[1:]
    direct_size = 0
    for line in lines:
      if line[:3] != 'dir':
        direct_size += int(line.split(' ')[0])
    sizes[''.join(path)] = direct_size
    if direct_size <= 100000:
      total += direct_size

    for i in range(1, len(path)):
      ancestor_path_key = ''.join(path[:i])
      ancestor_size = sizes[ancestor_path_key]
      if ancestor_size + direct_size <= 100000:
        total += direct_size
      elif ancestor_size <= 100000:
        total -= ancestor_size
      sizes[ancestor_path_key] += direct_size
      
  elif command[3:5] == '..':
    path.pop()
  else:
    folder = command[3:-1]
    path.append(folder)
    sizes[''.join(path)] = 0

print(total)

# recursive approach
def traverse(contents, _index=0):
  index = _index
  size = 0
  ret = 0
  childs_count = 0
  content = contents[index]
  lines = content.splitlines()
  for line in lines:
    if line[:3] == 'dir':
      childs_count += 1
    else:
      size += int(line.split(' ')[0])
  index += 1
  for _ in range(childs_count):
    result = traverse(contents, index)
    ret += result[0]
    size += result[1]
    index = result[2]
  if size <= 100000:
    ret += size
  if _index == 0:
    return ret
  return ret, size, index

contents = [command[3:] for command in list(filter(lambda x: x[:2] == 'ls', puzzle_input.split('$ ')[1:]))]
print(traverse(contents))
