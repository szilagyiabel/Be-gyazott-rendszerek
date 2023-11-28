from sense_hat import SenseHat
sense = SenseHat()
from time import sleep

# Define the functions
def red():
  
  for i in range(4):
    P = (255, 0, 0)
    O = (0,0,0)
    heart = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, O, P, P, O,
    P, P, P, P, P, P, P, P,
    P, P, P, P, P, P, P, P,
    O, P, P, P, P, P, P, O,
    O, O, P, P, P, P, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, O, O, O, O, O,
    ]

    sense.set_pixels(heart)
    sleep(1)
    sense.clear()
    sleep(1)
    
def blue():
  sense.clear(0, 0, 255)
def green():
  sense.clear(0, 255, 0)
def yellow():
  sense.clear(255, 255, 0)
  
sense.stick.direction_up = red
sense.stick.direction_down = blue
sense.stick.direction_left = green
sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear
while True:
  # do nothing
  pass