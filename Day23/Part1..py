import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
field = puzzle_input.splitlines()

elves = set()
for y in range(len(field)):
  for x in range(len(field[y])):
    if field[y][x] == '#':
      elves.add(complex(x, y))

round_count = 10
order = [0, 1, 2, 3]
for _ in range(round_count):
  moves = {}
  for elf in elves:
    n = [c + elf for c in (-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j)]
    done = True
    for c in n:
      if c in elves:
        done = False
        break
    if done:
      moves[elf] = elf
      continue
    for j in order:
      triplet =    ((n[0],n[1],n[2]),(n[5],n[6],n[7]),(n[0],n[3],n[5]),(n[2],n[4],n[7]))[j]
      if triplet[0] not in elves and triplet[1] not in elves and triplet[2] not in elves:
        if triplet[1] in moves:
          moves[triplet[1]] = None
        else:
          moves[triplet[1]] = elf
        break
    moves[elf] = elf
  new_elves = set()
  moved = set([None])
  for move, elf in moves.items():
    if elf not in moved:
      new_elves.add(move)
      moved.add(elf)
  elves = new_elves
  order.append(order.pop(0))

x_min = float('inf')
y_min = float('inf')
x_max = 0
y_max = 0
for elf in elves:
  x_min = min(elf.real, x_min)
  y_min = min(elf.imag, y_min)
  x_max = max(elf.real, x_max)
  y_max = max(elf.imag, y_max)

print(round((x_max - x_min + 1)*(y_max - y_min + 1) - len(elves)))

