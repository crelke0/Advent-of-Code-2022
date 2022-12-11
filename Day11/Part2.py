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
DIVISIBLE = 'divisible'
common_divisor = 1
for monkey_specs in puzzle_input.split('\n\n'):
  lines = monkey_specs.splitlines()[1:]
  items = [int(s) for s in lines[0].replace('  Starting items: ', '').split(', ')]
  operation = lines[1].replace('  Operation: new = old ', '').split(' ')
  if operation[1] != 'old':
    operation[1] = int(operation[1])
  divisibility = int(lines[2].replace('  Test: divisible by ', ''))
  common_divisor *= divisibility
  true_case = int(lines[3].replace('    If true: throw to monkey ', ''))
  false_case = int(lines[4].replace('    If false: throw to monkey ', ''))
  monkeys.append({ITEMS: items, OPERATION: operation, DIVISIBILITY: divisibility, TRUE_CASE: true_case, FALSE_CASE: false_case, ACTIVITY: 0, DIVISIBLE: [0]})

def bin_insert(lst, itm, low_bnd=0, up_bnd=None):
  if up_bnd == None:
    up_bnd = len(lst) - 1
  mid = (low_bnd + up_bnd)//2
  if mid == low_bnd:
    if lst[mid] < itm:
      mid += 1
    lst.insert(mid, itm)
    return lst
  if lst[mid] < itm:
    return bin_insert(lst, itm, mid, up_bnd)
  return bin_insert(lst, itm, low_bnd, mid)

for i in range(10000):
  for j in range(len(monkeys)):
    monkey = monkeys[j]
    monkey[ACTIVITY] += len(monkey[ITEMS])
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
      item = item%common_divisor
      if item%monkey[DIVISIBILITY] == 0:
        monkeys[monkey[TRUE_CASE]][ITEMS].append(item)
      else:
        monkeys[monkey[FALSE_CASE]][ITEMS].append(item)
      monkey[ITEMS] = monkey[ITEMS][1:]
largest = [0, 0]
for monkey in monkeys:
  largest.append(monkey[ACTIVITY])
  largest.remove(min(largest))
print(largest[0]*largest[1])
