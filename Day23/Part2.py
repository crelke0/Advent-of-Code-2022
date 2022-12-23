import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
field = puzzle_input.splitlines()

elves = set()
for y in range(len(field)):
  for x in range(len(field[y])):
    if field[y][x] == '#':
      elves.add(complex(x, y))

round_num = 0
order = [0, 1, 2, 3]
while True:
  round_num += 1
  moves = {}
  elf_moved = False
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
    elf_moved = True
    for j in order:
      triplet =    ((n[0],n[1],n[2]),(n[5],n[6],n[7]),(n[0],n[3],n[5]),(n[2],n[4],n[7]))[j]
      if triplet[0] not in elves and triplet[1] not in elves and triplet[2] not in elves:
        if triplet[1] in moves:
          moves[triplet[1]] = None
        else:
          moves[triplet[1]] = elf
        break
    moves[elf] = elf
  if not elf_moved:
    break
  new_elves = set()
  moved = set([None])
  for move, elf in moves.items():
    if elf not in moved:
      new_elves.add(move)
      moved.add(elf)
  elves = new_elves
  order.append(order.pop(0))

print(round_num)