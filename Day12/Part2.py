import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
grid = [list(line) for line in puzzle_input.splitlines()]

def heuristic(pos, end_pos):
  return pos[0] - end_pos[0] + pos[1] - end_pos[1]

start_pos = None
end_pos = None
HEIGHT = 'height'
H_COST = 'hcost'
G_COST = 'gcost'
LENGTH = 'length'
open_set = []
for x in range(len(grid)):
  for y in range(len(grid[x])):
    g_cost = float('inf')
    if grid[x][y] == 'S':
      grid[x][y] = 'a'
    elif grid[x][y] == 'E':
      grid[x][y] = 'z'
      end_pos = [x, y]
    if grid[x][y] == 'a':
      g_cost = 0
      open_set.append([x, y])
    grid[x][y] = {HEIGHT: ord(grid[x][y]) - 96, G_COST: g_cost, H_COST: 0, LENGTH: 0}

while len(open_set) != 0:
  lowest_f_cost = float('inf')
  current_pos = open_set[0]
  for pos in open_set:
    spot = grid[pos[0]][pos[1]]
    f_cost = spot[G_COST] + spot[H_COST]
    if f_cost < lowest_f_cost:
      lowest_f_cost = f_cost
      current_pos = pos
  cx, cy = current_pos
  if current_pos == end_pos:
    print(grid[cx][cy][LENGTH])
    break
  
  open_set.remove(current_pos)
  for neighbor_pos in [[cx - 1, cy], [cx + 1, cy], [cx, cy - 1], [cx, cy + 1]]:
    nx, ny = neighbor_pos
    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
      continue
    c_info = grid[cx][cy]
    n_info = grid[nx][ny]
    if n_info[HEIGHT] - c_info[HEIGHT] > 1:
      continue
    n_g_cost = c_info[G_COST] + 1
    if n_g_cost < n_info[G_COST]:
      n_info[LENGTH] = c_info[LENGTH] + 1
      n_info[G_COST] = n_g_cost
      n_info[H_COST] = heuristic([nx, ny], end_pos)
      if [nx, ny] not in open_set:
        open_set.append([nx, ny])
    