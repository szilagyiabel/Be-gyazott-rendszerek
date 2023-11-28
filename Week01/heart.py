from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

red = (255, 0, 0)
nothing = (0,0,0)


def heart():
    P = red
    O = nothing
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
    return heart

images = [heart]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1