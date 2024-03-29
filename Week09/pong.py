from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()

w = (0,0,0)
r = (255,255,255)

sense.clear(0, 0, 0)
score = 0
x = 4
ball_position=[6, 3]
ball_speed=[-1, -1]

def draw_bat():
    sense.set_pixel(0, x, 255, 255, 255)
    sense.set_pixel(0, x+1, 255, 255, 255)
    sense.set_pixel(0, x-1, 255, 255, 255)
        
def ball_play():
    global score
    sense.set_pixel(ball_position[0], ball_position[1], 0, 0, 0)

    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    if ball_position[1] == 0 or ball_position[1] == 7:
        ball_speed[1] = -ball_speed[1]
    if ball_position[0] == 7:
        ball_speed[0] = -ball_speed[0]
    if ball_position[0] == 1 and x-1 <= ball_position[1] <= x+1:
        score += 1
        ball_speed[0] = -ball_speed[0]
    if ball_position[0] == 0:
        return False

    sense.set_pixel(ball_position[0], ball_position[1], 0, 0, 255)
    return True

def move_up(event):
    global x
    if x > 1 and event.action=='pressed':
        x -= 1

def move_down(event):
    global x
    if x < 6 and event.action=='pressed':
        x += 1

sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

while ball_play():
    draw_bat()
    sleep(0.25)
    sense.clear(0, 0, 0)
    
sense.show_message('Game over!', scroll_speed=0.05, back_colour=w)
sense.show_message('Score: ' + str(score), scroll_speed=0.05, back_colour=w)