from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
pixel_list = sense.get_pixels()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

sense.set_pixel(0, 0, red) 
sense.set_pixel(0, 2, green)
sense.set_pixel(0, 4, blue)

orientation = sense.get_orientation_degrees()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

north = sense.get_compass()
print("north: %s" % north)

# alternatives
print(sense.compass)