from sense_hat import SenseHat
from time import sleep
import math

sense = SenseHat()

weather_dict = {
    1: "Settled Fine",
    2: "Fine Weather",
    3: "Fine, Becoming Less Settled",
    4: "Fairly Fine, Showery Later",
    5: "Showery, Becoming More Unsettled",
    6: "Unsettled, Rain Later",
    7: "Rain at Times, Worse Later",
    8: "Rain at Times, Becoming Very Unsettled",
    9: "Very Unsettled, Rain",
    10: "Settled Fine",
    11: "Fine Weather",
    12: "Fine, Possibly Showers",
    13: "Fairly Fine, Showers Likely",
    14: "Showery, Bright Intervals",
    15: "Changeable, Some Rain",
    16: "Unsettled, Rain at Times",
    17: "Rain at Frequent Intervals",
    18: "Very Unsettled, Rain",
    20: "Settled Fine",
    21: "Fine Weather",
    22: "Becoming Fine",
    23: "Fairly Fine, Improving",
    24: "Fairly Fine, Possibly Showers Early",
    25: "Showery Early, Improving",
    26: "Changeable, Mending",
    27: "Rather Unsettled, Clearing Later",
    28: "Unsettled, Probably Improving",
    29: "Unsettled, Short Fine Intervals",
    30: "Very Unsettled, Finer at Times",
    31: "Stormy, Possibly Improving",
    32: "Stormy, Much Rain"
}

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = 125
    
    t = round(t, 1)
    p = round(p, 1)


    P0 = p*pow((1 - (0.0065 * h) / (t + 0.0065 * h + 273.15)),-5.257)
     
    if 985 <= P0 and P0 <= 1050:
        z = 127 - 0.12 * P0
        print(weather_dict[z // 1])
    elif 960 <= P0 and P0 <= 1033:
        z = 144 - 0.13 * P0
        print(math.floor(weather_dict[z]))
    elif 947 <= P0 and P0 <= 1030:
        z = 185 - 0.16 * P0
        print(math.floor(weather_dict[z]))
    elif P0>1200:
      print()
         
    sleep(1)