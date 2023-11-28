from sense_hat import SenseHat
import time

sense = SenseHat()

state = 0

w = (255,255,255)
r = (255,0,0)
g = (0,255,0)
y = (255,255,0)
n = (0,0,0)
red = [
 n, n, n, r, r, n, n, n,
 n, n, n, r, r, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]
 
red_yellow = [
 n, n, n, r, r, n, n, n,
 n, n, n, r, r, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]
 
yellow = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]
 
green = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, g, g, n, n, n,
 n, n, n, g, g, n, n, n
 ]


def color_state(color, duration):  
  sense.set_pixels(color)
  time.sleep(duration)
  sense.clear()

def out_of_order_state():
  sense.set_pixels(yellow)
  time.sleep(0.5)
  sense.clear()
  time.sleep(0.5)
 
def set_state():
  global state
  if state < 3:
    state += 1
  elif state == 3:
    state = 0
  else:
    pass
 
def button_event(event):
  global state
  if event.action == 'released':
    if state != 4:
      state = 4
    else:
      state = 3

# orara erre tenni
#sense.stick.direction_middle = button_event
sense.stick.direction_up = button_event

while True:
  if state == 0:
    color_state(red,3)
  elif state == 1:
    color_state(red_yellow, 1)
  elif state == 2:
    color_state(green, 2)
  elif state == 3:
    color_state(yellow, 1)
  else:
    out_of_order_state()
  set_state()
