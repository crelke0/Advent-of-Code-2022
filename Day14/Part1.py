import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
solid = []
lowest = 0
for line in puzzle_input.splitlines():
  coords = [[int(s) for s in coords.split(',')] for coords in line.split(' -> ')]
  for i in range(len(coords) - 1):
    a, b = min(coords[i + 1][0], coords[i][0]), max(coords[i + 1][0], coords[i][0])
    for x in range(a, b + 1):
      a, b = min(coords[i][1], coords[i + 1][1]), max(coords[i + 1][1], coords[i][1])
      for y in range(a, b + 1):
        solid.append(complex(x, y))
        lowest = max(lowest, y)
counter = 0
while True:
  sand = 500 + 0j
  done = False
  while True:
    if sand + 1j not in solid:
      sand += 1j
    elif sand - 1 + 1j not in solid:
      sand += -1 + 1j
    elif sand + 1 + 1j not in solid:
      sand += 1 + 1j
    else:
      break
    if sand.imag > lowest:
      done = True
      break
  if done:
    break
  counter += 1
  solid.append(sand)
print(counter)