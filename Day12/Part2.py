import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
grid = [list(line) for line in puzzle_input.splitlines()]

start_pos = None
HEIGHT = 'height'
H_COST = 'hcost'
G_COST = 'gcost'
LENGTH = 'length'
for x in range(len(grid)):
  for y in range(len(grid[x])):
    g_cost = float('inf')
    if grid[x][y] == 'S':
      grid[x][y] = 'a'
    elif grid[x][y] == 'E':
      grid[x][y] = 'z'
      start_pos = [x, y]
      g_cost = 0
    grid[x][y] = {HEIGHT: ord(grid[x][y]) - 96, G_COST: g_cost, LENGTH: 0}

open_set = [start_pos]
while len(open_set) != 0:
  lowest_f_cost = float('inf')
  current_pos = open_set[0]
  for pos in open_set:
    spot = grid[pos[0]][pos[1]]
    f_cost = spot[G_COST]
    if f_cost < lowest_f_cost:
      lowest_f_cost = f_cost
      current_pos = pos
  cx, cy = current_pos
  if grid[cx][cy][HEIGHT] == 1:
    print(grid[cx][cy][LENGTH])
    break
  
  open_set.remove(current_pos)
  for neighbor_pos in [[cx - 1, cy], [cx + 1, cy], [cx, cy - 1], [cx, cy + 1]]:
    nx, ny = neighbor_pos
    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
      continue
    c_info = grid[cx][cy]
    n_info = grid[nx][ny]
    if c_info[HEIGHT] - n_info[HEIGHT] > 1:
      continue
    n_g_cost = c_info[G_COST] + 1
    if n_g_cost < n_info[G_COST]:
      n_info[LENGTH] = c_info[LENGTH] + 1
      n_info[G_COST] = n_g_cost
      if [nx, ny] not in open_set:
        open_set.append([nx, ny])
    