import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
monkeys = eval('{\'' + puzzle_input.replace('\n', '\',\'').replace(': ', '\':\'') + '\'}')
monkey1, op, monkey2 = monkeys['root'].split(' ')
monkeys['root'] = monkey1 + ' - ' + monkey2

def evaluate(monkeys, humn, monkey='root'):
  current_expression = monkeys[monkey]
  if monkey == 'humn':
    return humn
  if current_expression.isdigit():
    return int(current_expression)
  monkey1, op, monkey2 = current_expression.split(' ')
  return eval(str(evaluate(monkeys, humn, monkey1)) + op + str(evaluate(monkeys, humn, monkey2)))

def gradient_descent(guess, func):
  x1 = guess
  x2 = guess + 0.1
  y1 = func(x1)
  y2 = func(x2)
  return -y1*(x1 - x2)/(y1 - y2) + x1

func = lambda n: evaluate(monkeys, n)
guess = 0
while abs(func(guess)) > 0.1:
  guess = gradient_descent(guess, func)
print(round(guess))