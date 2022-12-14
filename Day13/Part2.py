import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
packets = [eval(line) for line in puzzle_input.replace('\n\n', '\n').splitlines()]

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

def quicksort(array, compare_func):
  if len(array) < 2:
    return array
  else: 
    pivot = array[0]
    less = [packet for packet in array[1:] if compare_func(packet, pivot)]
    greater = [packet for packet in array[1:] if compare_func(pivot, packet)]
    return quicksort(less, compare_func) + [pivot] + quicksort(greater, compare_func)

packets.append([[2]])
packets.append([[6]])
_sorted = quicksort(packets, compare)
print((_sorted.index([[2]]) + 1)*(_sorted.index([[6]]) + 1))