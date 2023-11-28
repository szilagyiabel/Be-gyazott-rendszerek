from sense_hat import SenseHat
sense = SenseHat()
from time import sleep

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