import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
puzzle_input = puzzle_input.splitlines()

def heuristic(pos, end):
  return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

width = len(puzzle_input)
height = len(puzzle_input[0])
blizards = {}
walls = []
for x in range(width):
  for y in range(height):
    if puzzle_input[x][y] == '.':
      if x == 0:
        start_pos = (x, y, 0)
      elif x == width - 1:
        end_pos = (x, y)
    elif puzzle_input[x][y] in '<>^v':
      direction = ((0, -1), (0, 1), (-1, 0), (1, 0))['<>^v'.index(puzzle_input[x][y])]
      if (x, y) in blizards:
        blizards[(x, y)].append(direction)
      else:
        blizards[(x, y)] = [direction]
    elif puzzle_input[x][y] == '#':
      walls.append((x, y))

walls = set(walls)

def step_blizards(blizards, width, height):
  new_blizards = {}
  for pos, directions in blizards.items():
    for direction in directions:
      new_pos = ((pos[0] + direction[0] - 1)%(width - 2) + 1, (pos[1] + direction[1] - 1)%(height - 2) + 1)
      if new_pos in new_blizards:
        new_blizards[new_pos].append(direction)
      else:
        new_blizards[new_pos] = [direction]
  return new_blizards

g_costs = {start_pos: 0}
h_costs = {start_pos[:-1]: heuristic(start_pos, end_pos)}
timed_blizards = [blizards]
_open = [start_pos]
while len(_open):
  current_g_cost = None
  lowest_f_cost = float('inf')
  for pos in _open:
    g_cost = g_costs[pos]
    f_cost = g_cost + h_costs[pos[:-1]]
    if f_cost < lowest_f_cost:
      lowest_f_cost = f_cost
      current_g_cost = g_cost
      current_pos = pos
  while current_pos in _open:
    _open.remove(current_pos)

  x = current_pos[0]
  y = current_pos[1]
  t = current_pos[2]
  done = False
  if t + 1 == len(timed_blizards):
    timed_blizards.append(step_blizards(timed_blizards[-1], width, height))
  for n in ((x - 1, y, t + 1), (x + 1, y, t + 1), (x, y - 1, t + 1), (x, y + 1, t + 1), (x, y, t + 1)):
    nxy = n[:-1]
    if n[0] < 0 or nxy in walls or nxy in timed_blizards[n[2]]: continue
    if nxy == end_pos:
      print(current_g_cost + 1)
      done = True
      break
    if n not in g_costs:
      g_costs[n] = current_g_cost + 1
      h_costs[nxy] = heuristic(n, end_pos)
    else:
      if current_g_cost + 1 < g_costs[n]:
        g_costs[n] = current_g_cost + 1
    _open.append(n)
  if done:
    break
