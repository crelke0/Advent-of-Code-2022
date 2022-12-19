import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
cubes = [[int(c) for c in coord.split(',')] for coord in puzzle_input.splitlines()]
sides = []
for cube in cubes:
  for i in range(3):
    new_side = cube + [i]
    if new_side in sides:
      sides.remove(new_side)
    else:
      sides.append(new_side)

    ref_cube = cube.copy()
    ref_cube[i] -= 1
    new_side = ref_cube + [i]
    if new_side in sides:
      sides.remove(new_side)
    else:
      sides.append(new_side)
print(len(sides))