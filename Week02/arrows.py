from sense_hat import SenseHat
sense = SenseHat()
from time import sleep

# Define the functions
def right():
  P = (255, 0, 0)
  O = (0,0,0)
  
  heart = [
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, P, O, O, O,
  O, O, O, O, O, P, O, O,
  O, P, P, P, P, P, P, O,
  O, O, O, O, O, P, O, O,
  O, O, O, O, P, O, O, O,
  O, O, O, O, O, O, O, O,
  ]
  sense.set_pixels(heart)
    
def up():
  P = (255, 0, 0)
  O = (0,0,0)
  
  heart = [
  O, O, O, O, O, O, O, O,
  O, O, O, P, O, O, O, O,
  O, O, P, P, P, O, O, O,
  O, P, O, P, O, P, O, O,
  O, O, O, P, O, O, O, O,
  O, O, O, P, O, O, O, O,
  O, O, O, P, O, O, O, O,
  O, O, O, O, O, O, O, O,
  ]
  sense.set_pixels(heart)
  
def down():
  P = (255, 0, 0)
  O = (0,0,0)
  
  heart = [
  O, O, O, O, O, O, O, O,
  O, O, O, P, O, O, O, O,
  O, O, O, P, O, O, O, O,
  O, O, O, P, O, O, O, O,
  O, P, O, P, O, P, O, O,
  O, O, P, P, P, O, O, O,
  O, O, O, P, O, O, O, O,
  O, O, O, O, O, O, O, O,
  ]
  sense.set_pixels(heart)
  
def left():
  P = (255, 0, 0)
  O = (0,0,0)
  
  heart = [
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, P, O, O, O, O,
  O, O, P, O, O, O, O, O,
  O, P, P, P, P, P, P, O,
  O, O, P, O, O, O, O, O,
  O, O, O, P, O, O, O, O,
  O, O, O, O, O, O, O, O,
  ]
  sense.set_pixels(heart)
  
sense.stick.direction_up = up
sense.stick.direction_down = down
sense.stick.direction_left = left
sense.stick.direction_right = right
sense.stick.direction_middle = sense.clear
while True:
  # do nothing
  pass