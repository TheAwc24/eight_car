#!/usr/bin/python3

import os
import random
import adafruit_dotstar
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# Switcher variables (for the different modes)
switcher = DigitalInOut(board.D17)
switcher.direction = Direction.INPUT
switcher.pull = Pull.UP
MODE = 0

# Eight button variables
button = DigitalInOut(board.D23)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Sound variables
TRACK = ""
CLIP = ["eight", "8game_6_00", "bark4", "klaxon1", "raphael1", "raphael2", "raphael3", "raphael4", "raphael5", "raphael6", "raphael7", "raphael8", "raphael9", "raphael10", "ui_buttons_b_01", "ui_buttons_b_02", "ui_buttons_b_03"]

# Light variables
DOTSTAR_DATA = board.D5
DOTSTAR_CLOCK = board.D6
dots = adafruit_dotstar.DotStar(DOTSTAR_CLOCK, DOTSTAR_DATA, 3, brightness=0.2)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)

# Eight Button Function
def eight():
    while True:
        if not button.value:
            TRACK = CLIP[random.randrange(0,16)]
            os.system(f"flac -d -c 'sounds/{TRACK}.flac' | aplay")
        time.sleep(0.01)

# Fun Button Function
def fun():
    while True:
        if not button.value:
            os.system(f"flac -d -c 'sounds/{CLIP[0]}.flac' | aplay")
        time.sleep(0.01)

# All Sounds Function
def all_sounds():
    TRACK = CLIP[random.randrange(0,16)]
    os.system(f"flac -d -c 'sounds/{TRACK}.flac' | aplay")

# Main loop
while True:
    # Switch mode if button is pressed
    if not switcher.value:
        if MODE == 2:
            MODE = 0
        else:
            MODE+=1

    # Select function based on mode
    if MODE == 0:
        dots[0]= (WHITE)
        dots[1] = (RED)
        dots[2] = (WHITE)
        eight()
    elif MODE == 1:
        dots[0] = (RED)
        dots[1] = (GREEN)
        dots[2] = (RED)
        fun()
    elif MODE == 2:
        dots[0] = (BLUE)
        dots[1] = (YELLOW)
        dots[2] = (BLUE)
        all_sounds()
    else:
        dots[0] = (RED)
        dots[1] = (WHITE)
        dots[2] = (RED)
        eight()

    time.sleep(0.01)