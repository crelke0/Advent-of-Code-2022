import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
board, string = puzzle_input.split('\n\n')
directions = []

# parse directions
while len(string):
  for i in range(len(string) + 1):
    if i == len(string) or not string[i].isdigit():
      break
  if i == 0:
    i = 1
    directions.append(string[0])
  else:
    directions.append(int(string[:i]))
  string = string[i:]
board = board.splitlines()
net_height = len(board)
net_width = 0
for row in board:
  net_width = max(net_width, len(row))
width = min(net_width, net_height)//3

# class for each cube side
class Side:
  def __init__(self, board, grid_pos):
    self.board = board
    self.grid_pos = grid_pos
    self.neighbors = {}
  def add_neighbor(self, dir, side, transform):
    self.neighbors[dir] = [side, transform]

# adding all the sides to a dictionary which has keys that represent their place on the map
sides = {}
for gx in range(4):
  for gy in range(4):
    x = gx*width
    y = gy*width
    if y >= len(board) or x >= len(board[y]) or board[y][x] == ' ':
      continue
    side_board = []
    for row in board[y:y+width]:
      side_board.append(row[x:x+width])
    sides[(gx, gy)] = Side(side_board, (gx, gy))

# find the edges that are already given in the net
for pos, side in sides.items():
  for n in range(4):
    nx = pos[0]+1-n if n%2 == 0 else pos[0]
    ny = pos[1]+2-n if n%2 != 0 else pos[1]
    if (nx, ny) in sides:
      side.neighbors[n] = [0, sides[(nx, ny)]]

# find the rest of the edges
while True:
  done = True
  for side in sides.values():
    make_edge = False
    for key1 in side.neighbors.keys():
      key2 = None
      if (key1 + 1)%4 in side.neighbors:
        key2 = (key1 + 1)%4
      elif (key1 - 1)%4 in side.neighbors:
        key2 = (key1 - 1)%4
      else:
        continue

      make_edge = True
      for n in side.neighbors[key1][1].neighbors.values():
        if n[1] == side.neighbors[key2][1]:
          make_edge = False
          break
      if make_edge:
        break
    if make_edge:
      transform = (key2 + side.neighbors[key2][0]) - (key1 + side.neighbors[key1][0])
      side.neighbors[key1][1].neighbors[(key2 + side.neighbors[key1][0])%4] = [transform, side.neighbors[key2][1]]
      side.neighbors[key2][1].neighbors[(key1 + side.neighbors[key2][0])%4] = [-transform, side.neighbors[key1][1]]
      done = False
  if done: break

# find starting place
grid_pos = (float('inf'), float('inf'))
for pos in sides.keys():
  if pos[1] < grid_pos[1]:
    grid_pos = pos
  if pos[1] == grid_pos[1] and pos[0] < grid_pos[0]:
    grid_pos = pos

# walk along cube
x = 0
y = 0
dx = 1
dy = 0
for direction in directions:
  if direction == 'L':
    dx, dy = dy, -dx
  elif direction == 'R':
    dx, dy = -dy, dx
  else:
    for _ in range(direction):
      old_x, old_y, old_dx, old_dy, old_g = x, y, dx, dy, grid_pos
      x += dx
      y += dy
      transform = 0
      if x == -1 or x == width:
        transform, neighbor = sides[grid_pos].neighbors[0 if x == width else 2]
        transform %= 4
        grid_pos = neighbor.grid_pos
        x = width - abs(x)
      elif y == -1 or y == width:
        transform, neighbor = sides[grid_pos].neighbors[1 if y == width else 3]
        transform %= 4
        grid_pos = neighbor.grid_pos
        y = width - abs(y)

      while transform != 0:
        transform -= 1
        dx, dy = -dy, dx
        x, y = width - 1 - y, x

      if sides[grid_pos].board[y][x] == '#':
        x, y, dx, dy, grid_pos = old_x, old_y, old_dx, old_dy, old_g
        break


print((y + 1 + grid_pos[1]*width)*1000 + (x + 1 + grid_pos[0]*width)*4 + (2 - dy) * abs(dy))