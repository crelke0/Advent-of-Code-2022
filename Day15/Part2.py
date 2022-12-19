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

valid_points = []
for sensor_a in sensors:
  for sensor_b in sensors:
    h1 = sensor_a[POS][0]
    k1 = sensor_a[POS][1]
    r1 = sensor_a[DIST] + 1
    h2 = sensor_b[POS][0]
    k2 = sensor_b[POS][1]
    r2 = sensor_b[DIST] + 1
    for n in range(8):
      binary = bin(n)[2:].ljust(3, '0')
      s = int(binary[0])*2 - 1
      a1 = int(binary[1])*2 - 1
      a2 = int(binary[2])*2 - 1
      # formula for finding intersection points between two sensor bounds
      x1 = (h2*s-a2*s*r2+k2+h1*s-a1*s*r1-k1)//(2*s)
      y1 = s*(x1-h1+a1*r1)+k1
      if [x1, y1] not in valid_points:
        valid_points.append([x1, y1])

for point in valid_points:
  done = True
  for sensor in sensors:
    if manhatten(sensor[POS], point) <= sensor[DIST] or not (0 <= point[0] <= 4000000 and 0 <= point[1] <= 4000000):
      done = False
  if done:
    print(point[0]*4000000+point[1])
    break
