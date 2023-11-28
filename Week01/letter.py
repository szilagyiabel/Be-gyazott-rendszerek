from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.show_letter("-", text_colour=(255,255,255), back_colour=(0,0,0)) and sense.show_letter(">", text_colour=(255,255,255), back_colour=(0,0,0))

def number_gen(event):
    if event.action == "pressed":
      val = random.randint(1,6)
      print(val)