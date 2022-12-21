import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
monkeys = eval('{\'' + puzzle_input.replace('\n', '\',\'').replace(': ', '\':\'') + '\'}')

def evaluate(monkeys, monkey='root'):
  current_expression = monkeys[monkey]
  if current_expression.isdigit():
    return int(current_expression)
  monkey1, op, monkey2 = current_expression.split(' ')
  return eval(str(evaluate(monkeys, monkey1)) + op + str(evaluate(monkeys, monkey2)))

print(round(evaluate(monkeys)))