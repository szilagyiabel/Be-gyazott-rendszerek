from sense_hat import SenseHat
import time
import random

sense = SenseHat()

o = (0,0,0)
b = (255,255,255)

def one():
    one = [o,o,o,o,o,o,o,o,
           o,o,o,o,o,o,o,o,
           o,o,o,o,o,o,o,o,
           o,o,o,b,b,o,o,o,
           o,o,o,b,b,o,o,o,
           o,o,o,o,o,o,o,o,
           o,o,o,o,o,o,o,o,
           o,o,o,o,o,o,o,o]
    return one

def two():
  two = [o,o,o,o,o,o,o,o,
             o,b,b,o,o,o,o,o,
             o,b,b,o,o,o,o,o,
             o,o,o,o,o,o,o,o,
             o,o,o,o,o,o,o,o,
             o,o,o,o,o,b,b,o,
             o,o,o,o,o,b,b,o,
             o,o,o,o,o,o,o,o]
  return two

def three():
  three = [b,b,o,o,o,o,o,o,
               b,b,o,o,o,o,o,o,
               o,o,o,o,o,o,o,o,
               o,o,o,b,b,o,o,o,
               o,o,o,b,b,o,o,o,
               o,o,o,o,o,o,o,o,
               o,o,o,o,o,o,b,b,
               o,o,o,o,o,o,b,b]
  return three

def four():
  four =  [b,b,o,o,o,o,b,b,
             b,b,o,o,o,o,b,b,
             o,o,o,o,o,o,o,o,
             o,o,o,o,o,o,o,o,
             o,o,o,o,o,o,o,o,
             o,o,o,o,o,o,o,o,
             b,b,o,o,o,o,b,b,
             b,b,o,o,o,o,b,b]
  return four

def five():
  five =  [b,b,o,o,o,o,b,b,
               b,b,o,o,o,o,b,b,
               o,o,o,o,o,o,o,o,
               o,o,o,b,b,o,o,o,
               o,o,o,b,b,o,o,o,
               o,o,o,o,o,o,o,o,
               b,b,o,o,o,o,b,b,
               b,b,o,o,o,o,b,b]
  return five
    
def six():
  six  =   [b,b,o,b,b,o,b,b,
               b,b,o,b,b,o,b,b,
               o,o,o,o,o,o,o,o,
               o,o,o,o,o,o,o,o,
               o,o,o,o,o,o,o,o,
               o,o,o,o,o,o,o,o,
               b,b,o,b,b,o,b,b,
               b,b,o,b,b,o,b,b]
  return six

images = [one, two, three, four, five, six]
count = 0

def number_gen(event):
    if event.action == "pressed":
      val = random.randint(1,6)
      print(val)
      if val == 1:
        sense.set_pixels(one)
      elif val == 2:
        sense.set_pixels(two)
      elif val == 3:
        sense.set_pixels(three)
      elif val == 4:
        sense.set_pixels(four)
      elif val == 5:
        sense.set_pixels(five)
      elif val == 6:
        sense.set_pixels(six)
    
    sense.clear()

while True: 
    val = random.randint(1,6)
    sense.set_pixels(images[val % len(images)]())
    time.sleep(.75)
    print(val)