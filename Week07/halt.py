from sense_hat import SenseHat
import time

sense = SenseHat()
state = 0

w = (255, 255, 255)
r = (255, 0, 0)
g = (0, 255, 0)
y = (255, 255, 0)
n = (0, 0, 0)
ry = (0,255,255)

paused = False
actual_state = 0

#pixels = [[n] * 8 for _ in range(8)]  # Kezdetben minden cella fekete

def traffic_light_state(color, duration):
    sense.clear()
    if color == r:  # Piros állapot
        sense.set_pixel(3, 0, r)
        sense.set_pixel(4, 0, r)
        sense.set_pixel(3, 1, r)
        sense.set_pixel(4, 1, r)
    elif color == y:  # Sárga állapot
        sense.set_pixel(3, 3, y)
        sense.set_pixel(4, 3, y)
        sense.set_pixel(3, 4, y)
        sense.set_pixel(4, 4, y)
    elif color == g:  # Sárga állapot
        sense.set_pixel(3, 6, g)
        sense.set_pixel(4, 6, g)
        sense.set_pixel(3, 7, g)
        sense.set_pixel(4, 7, g)
    elif color == ry:  # Piros és sárga egyszerre
        sense.set_pixel(3, 0, r)
        sense.set_pixel(4, 0, r)
        sense.set_pixel(3, 1, r)
        sense.set_pixel(4, 1, r)
        sense.set_pixel(3, 3, y)
        sense.set_pixel(4, 3, y)
        sense.set_pixel(3, 4, y)
        sense.set_pixel(4, 4, y)
       
    time.sleep(duration)



def out_of_order_state():
    all_black = [(0, 0, 0)] * 64  # 64 fekete pixel
    sense.set_pixels(all_black)  # Minden cella fekete
    time.sleep(0.5)
    sense.clear()
    time.sleep(0.5)

def set_state():
    global state
    if state < 3:
        state += 1
    elif state == 3:
        state = 0

def button_event(event):
    global state
    if event.action == 'released':
        if state != 4:
            state = 4
        else:
            state = 3
           
def toggle_pause(event):
    global state
    global actual_state
    global paused
    if event.action == 'pressed':
        paused = not paused
        if not paused:
            actual_state = state


sense.stick.direction_down = button_event
sense.stick.direction_up = toggle_pause

while True:
  if not paused:
    if state == 0:
      traffic_light_state(r, 0.5)
      actual_state = 0
    elif state == 1:
      traffic_light_state(ry, 0.5)
      actual_state = 1
    elif state == 2:
      traffic_light_state(g, 0.5)
      actual_state = 2
    elif state == 3:
      traffic_light_state(y, 0.5)
      actual_state = 0
    else:
      out_of_order_state()
    set_state()