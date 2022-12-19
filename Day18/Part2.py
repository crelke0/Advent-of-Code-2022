import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
cubes = []
ranges = [[float('inf'), 0] for _ in range(3)]
for line in puzzle_input.splitlines():
  cube = [int(c) for c in line.split(',')]
  for c in range(3):
    # no idea why this has to be + and - 4. why doesn't just 1 work??
    ranges[c][0] = min(ranges[c][0], cube[c] - 4)
    ranges[c][1] = max(ranges[c][1], cube[c] + 4)
  cubes.append(cube)

def in_range(cube, ranges):
  for c in range(3):
    if not ranges[c][0] <= cube[c] <= ranges[0][1]:
      return False
  return True

surface_area = 0
stack = [[ranges[0][0], ranges[1][0], ranges[2][0]]]
checked = []
while len(stack):
  current = stack.pop()
  for i in range(6):
    c1 = i%3
    s = -1 if i > 2 else 1
    neighbor = current.copy()
    neighbor[c1] += s
    if neighbor in stack or neighbor in checked or not in_range(neighbor, ranges):
      continue
    if neighbor in cubes:
      surface_area += 1
      continue
    stack.append(neighbor)
  checked.append(current)
print(surface_area)