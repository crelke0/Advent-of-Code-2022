import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
solid = [[False]*1000 for _ in range(1000)]
lowest = 0
for line in puzzle_input.splitlines():
  coords = [[int(s) for s in coords.split(',')] for coords in line.split(' -> ')]
  for i in range(len(coords) - 1):
    a, b = min(coords[i + 1][0], coords[i][0]), max(coords[i + 1][0], coords[i][0])
    for x in range(a, b + 1):
      a, b = min(coords[i][1], coords[i + 1][1]), max(coords[i + 1][1], coords[i][1])
      for y in range(a, b + 1):
        solid[x][y] = True
        lowest = max(lowest, y)
solid += [False]*len(solid)
lowest += 2
counter = 0
while True:
  counter += 1
  x = 500
  y = 0
  while True:
    if not solid[x][y + 1]:
      y += 1
    elif not solid[x - 1][y + 1]:
      x -= 1
      y += 1
    elif not solid[x + 1][y + 1]:
      x += 1
      y += 1
    else:
      break
    if y == lowest:
      y = lowest - 1
      break
  if x == 500 and y == 0:
    break
  solid[x][y] = True
print(counter)