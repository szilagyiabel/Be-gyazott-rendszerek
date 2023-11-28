from sense_hat import SenseHat
sense = SenseHat()
#filename = ‘compass.txt’

file = open(filename, ‘w’)
sense.stick.direction_middle = stop
print(‘Start data acquisition…’)

#calibration process

while calibration:
  magnet = sense.get_compass_raw()
  x = magnet[‘x’]
  y = magnet[‘y’]
  file.wtite(str(x) + ‘,’ + str(y) + ‘\n’)
  
file.close()
xmax, xmin, ymax, ymin = plot(filename)

while True:
  magnet = sense.get_compass_raw()
  x = magnet[‘x’]
  y = magnet[‘y’]
  #range transform
  xz = -1 + ((1-(-1)) / (xmax - xmin)) * (x - xmin)
  yz = -1 + ((1-(-1)) / (ymax - ymin)) * (y - ymin)
  #degree (a) calculation
  if xz == 0 and yz < 0:
  deg = 90
  elif xz == 0 and yz > 0:
  deg = 270
  elif yz < 0:
  deg = 360 + math.atan2(yz, xz) * (180/3.14159)
  else:
  deg = math.atan2(yz, xz) * (180/3.14159)
#cardinal points
if deg < 45 or deg > 315:
sense.show_letter(‘N’)
elif deg < 135:
sense.show_letter(‘E’)
elif deg < 225:
sense.show_letter(‘S’)
else:
sense.show_letter(‘W’)
time.sleep(0.2)
sense.clear()