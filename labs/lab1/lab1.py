"""
Copyright MIT and Harvey Mudd College
MIT License
Summer 2020

Lab 1 - Driving in Shapes
"""

########################################################################################
# Imports
########################################################################################

from re import X
from shutil import SpecialFileError
import sys

sys.path.insert(1, "../../library")
import racecar_core
import racecar_utils as rc_utils

########################################################################################
# Global variables
########################################################################################

rc = racecar_core.create_racecar()

# Put any global variables here
mode = 0
counter = 0
########################################################################################
# Functions
########################################################################################


def start():
    """
    This function is run once every time the start button is pressed
    """
    # Begin at a full stop
    rc.drive.stop()
    global mode, counter
    mode = 0
    counter = 0
    # Print start message
    # TODO (main challenge): add a line explaining what the Y button does
    print(
        ">> Lab 1 - Driving in Shapes\n"
        "\n"
        "Controls:\n"
        "    Right trigger = accelerate forward\n"
        "    Left trigger = accelerate backward\n"
        "    Left joystick = turn front wheels\n"
        "    A button = drive in a circle\n"
        "    B button = drive in a square\n"
        "    X button = drive in a figure eight\n"
        "    Y button = drive in a triangle\n"
    )


def update():
    """
    After start() is run, this function is run every frame until the back button
    is pressed
    """
    # TODO (warmup): Implement acceleration and steering
    global mode, counter
    
    if rc.controller.was_pressed(rc.controller.Button.A) and mode == 0:
        counter = 0
        mode = 1
        print("Driving in a circle...",mode)

    if rc.controller.was_pressed(rc.controller.Button.B) and mode == 0:
        counter = 0  
        mode = 2
        print("Driving in a square...")

    if (mode == 0):
        speed = rc.controller.get_trigger(rc.controller.Trigger.RIGHT) - rc.controller.get_trigger(rc.controller.Trigger.LEFT)
        turn = rc.controller.get_joystick(rc.controller.Joystick.LEFT)[0]
        rc.drive.set_speed_angle(speed,turn)
        
    if (mode == 1):
        turn = 6
        if (counter < turn) : rc.drive.set_speed_angle(1,1)
        else : 
            rc.drive.stop()
            mode = 0

    if (mode == 2) :
        straight = 2
        turn = 1.32
        if (counter < straight) : rc.drive.set_speed_angle(1,0)
        elif (counter < straight + turn) : rc.drive.set_speed_angle(1, 1)
        elif (counter < 2 * straight + turn) : rc.drive.set_speed_angle(1, 0)
        elif (counter < 2 * straight + 2 * turn) : rc.drive.set_speed_angle(1, 1)
        elif (counter < 3 * straight + 2 * turn) : rc.drive.set_speed_angle(1, 0)
        elif (counter < 3 * straight + 3 * turn) : rc.drive.set_speed_angle(1, 1)
        elif (counter < 4 * straight + 3 * turn) : rc.drive.set_speed_angle(1, 0)
        elif (counter < 4 * straight + 4 * turn) : rc.drive.set_speed_angle(1, 1)
        else : 
            rc.drive.stop()
            mode = 0
    counter += rc.get_delta_time()   
    
        # TODO (main challenge): Drive in a square when the B button is pressed

    # TODO (main challenge): Drive in a figure eight when the X button is pressed

    # TODO (main challenge): Drive in a shape of your choice when the Y button
    # is pressed


########################################################################################
# DO NOT MODIFY: Register start and update and begin execution
########################################################################################

if __name__ == "__main__":
    rc.set_start_update(start, update)
    rc.go()
