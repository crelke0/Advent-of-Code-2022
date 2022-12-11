import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()
monkeys = []
ITEMS = 'items'
OPERATION = 'operation'
DIVISIBILITY = 'divisibility'
TRUE_CASE = 'true_case'
FALSE_CASE = 'false_case'
ACTIVITY = 'activity'
for monkey_specs in puzzle_input.split('\n\n'):
  lines = monkey_specs.splitlines()[1:]
  items = [int(s) for s in lines[0].replace('  Starting items: ', '').split(', ')]
  operation = lines[1].replace('  Operation: new = old ', '').split(' ')
  if operation[1] != 'old':
    operation[1] = int(operation[1])
  divisibility = int(lines[2].replace('  Test: divisible by ', ''))
  true_case = int(lines[3].replace('    If true: throw to monkey ', ''))
  false_case = int(lines[4].replace('    If false: throw to monkey ', ''))
  monkeys.append({ITEMS: items, OPERATION: operation, DIVISIBILITY: divisibility, TRUE_CASE: true_case, FALSE_CASE: false_case, ACTIVITY: 0})

largest = [0, 0]
for i in range(20):
  for monkey in monkeys:
    monkey[ACTIVITY] += len(monkey[ITEMS])
    largest.append(monkey[ACTIVITY])
    largest.remove(min(largest))
    for item in monkey[ITEMS]:
      operation = monkey[OPERATION]
      if operation[1] == 'old':
        a = item
      else:
        a = operation[1]
      if operation[0] == '*':
        item *= a
      else:
        item += a
      item //= 3
      if item%monkey[DIVISIBILITY] == 0:
        monkeys[monkey[TRUE_CASE]][ITEMS].append(item)
      else:
        monkeys[monkey[FALSE_CASE]][ITEMS].append(item)
      monkey[ITEMS] = monkey[ITEMS][1:]

print(largest[0]*largest[1])
