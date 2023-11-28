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
while True:
  for event in sense.stick.get_events():
      if event.action == "pressed":
        if event.direction == "middle":
          a = 0
          while a < 1:
            val = random.randint(0,5)
            sense.set_pixels(images[val]())
            time.sleep(.3)
            a+=1
            print(val+1)
