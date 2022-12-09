import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
instructions = puzzle_input.splitlines()
length = 10
snake = [[0, 0] for _ in range(length)]
visted = [[0, 0]]
for instruction in instructions:
  for n in range(int(instruction[2:])):
    snake_previous = [seg.copy() for seg in snake]
    snake[0][0 if instruction[0] in 'LR' else 1] += -1 if instruction[0] in 'UL' else 1
    for i in range(1, length):
      if abs(snake[i][0] - snake[i - 1][0]) > 1 or abs(snake[i][1] - snake[i - 1][1]) > 1:
        if snake[i][0] != snake[i - 1][0]:
          diff = snake[i - 1][0] - snake[i][0]
          snake[i][0] += diff // abs(diff)

        if snake[i][1] != snake[i - 1][1]:
          diff = snake[i - 1][1] - snake[i][1]
          snake[i][1] += diff // abs(diff)

    if snake[-1] not in visted:
      visted.append(snake[-1].copy())
print(len(visted))
