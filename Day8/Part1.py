import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
grid = [[int(c) for c in list(line)] for line in puzzle_input.splitlines()]
total = 0
for x in range(len(grid)):
  for y in range(len(grid[x])):
    current = grid[x][y]
    left_visible = True
    right_visible = True
    for x1 in range(len(grid)):
      if x1 == x: continue
      if current <= grid[x1][y]:
        if x1 < x:
          left_visible = False
        else:
          right_visible = False
    top_visible = True
    bottom_visible = True
    for y1 in range(len(grid[x])):
      if y1 == y: continue
      if current <= grid[x][y1]:
        if y1 < y:
          top_visible = False
        else:
          bottom_visible = False
    
    if left_visible or right_visible or top_visible or bottom_visible:
      total += 1

print(total)
