import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as input_file:
  puzzle_input = input_file.read()

def manhatten(pos1, pos2):
  return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

sensors = []
POS = 'pos'
DIST = 'dist'
for line in puzzle_input.splitlines():
  sensor, beacon = line.replace('Sensor at x=', '').split(': closest beacon is at x=')
  sensor = [int(s) for s in sensor.split(', y=')]
  beacon = [int(s) for s in beacon.split(', y=')]
  dist = manhatten(sensor, beacon)
  sensors.append({POS: sensor, DIST: dist})

def check_line(sensors, y, d):
  x = 0
  while True:
    possible_beacon = True
    for sensor in sensors:
      if manhatten([x, y], sensor[POS]) <= sensor[DIST]:
        possible_beacon = False
        break
    if possible_beacon:
      break
    x += d
  return abs(x) - 1
print(check_line(sensors, 2000000, -1) + check_line(sensors, 2000000, 1))