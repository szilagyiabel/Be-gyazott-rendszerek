from sense_hat import SenseHat
import time 
import math

sense = SenseHat()
while True:
  sea_level_pressure = 1013.25 
  pressure_change_per_meter = 0.012  
  
  current_pressure = sense.get_pressure()
  
  altitude = 44331 * (1 - pow((current_pressure / sea_level_pressure), 1/5.257))

  print(altitude)
  time.sleep(1)
