import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
board, string = puzzle_input.split('\n\n')
directions = []
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
for x in range(len(board[0])):
  if board[0][x] == '.':
    break
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
      ox, oy = x, y
      x += dx
      y += dy
      if y < 0 or y >= len(board) or x < 0 or x >= len(board[y]) or board[y][x] == ' ':
        x -= dx
        y -= dy
        while 0 <= y < len(board) and 0 <= x < len(board[y]) and board[y][x] != ' ':
          x -= dx
          y -= dy
        x += dx
        y += dy
      if board[y][x] == '#':
        x = ox
        y = oy
        break

print((y + 1)*1000 + (x + 1)*4 + (1 - dx) * abs(dx) + (2 - dy) * abs(dy))