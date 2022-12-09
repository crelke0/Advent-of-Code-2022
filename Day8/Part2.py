import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
grid = [[int(c) for c in list(line)] for line in puzzle_input.splitlines()]
best_score = 0
for x in range(len(grid)):
  for y in range(len(grid[x])):
    current = grid[x][y]
    left_distance = x
    right_distance = len(grid) - x - 1
    for x1 in range(len(grid)):
      if x1 == x: continue
      if current <= grid[x1][y]:
        if x1 < x:
          left_distance = min(left_distance, x - x1)
        else:
          right_distance = min(right_distance, x1 - x)
    top_distance = y
    bottom_distance = len(grid[x]) - y - 1
    for y1 in range(len(grid[x])):
      if y1 == y: continue
      if current <= grid[x][y1]:
        if y1 < y:
          top_distance = min(top_distance, y - y1)
        else:
          bottom_distance = min(bottom_distance, y1 - y)
    
    best_score = max(best_score, left_distance*right_distance*top_distance*bottom_distance)

print(best_score)
