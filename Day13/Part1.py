import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
pairs = [[eval(line) for line in pair.splitlines()] for pair in puzzle_input.split('\n\n')]

def compare(packet1, packet2):
  if packet1 == packet2:
    return None
  if type(packet1) == int and type(packet2) == int:
    return packet1 < packet2
  if type(packet1) == int:
    packet1 = [packet1]
  elif type(packet2) == int:
    packet2 = [packet2]
  for i in range(len(packet1)):
    if len(packet2) == i:
      return False
    is_right_order = compare(packet1[i], packet2[i])
    if is_right_order != None:
      return is_right_order
  if len(packet2) != len(packet1):
    return True
  return None

total = 0
for i in range(len(pairs)):
  total += compare(pairs[i][0], pairs[i][1]) * (i + 1)
print(total)
