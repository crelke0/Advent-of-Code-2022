import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
mix = [int(s) for s in puzzle_input.splitlines()]
order = [n for n in range(len(mix))]
for i in range(len(order)):
  current_index = order.index(i)
  n = mix[current_index]
  new_index = current_index + n
  new_index = new_index%(len(order) - 1)
  del mix[current_index]
  del order[current_index]
  mix.insert(new_index, n)
  order.insert(new_index, i)
  
zero_index = mix.index(0)
x = mix[(zero_index + 1000)%len(order)]
y = mix[(zero_index + 2000)%len(order)]
z = mix[(zero_index + 3000)%len(order)]
print(x+y+z)