#Import library that lets you control the Pi's GPIO pins
import RPi.GPIO as io

# Disable messages about GPIO pins already being in use
io.setwarnings(False)
# Numbering scheme that corresponds to breakout board and pin layout 
io.setmode(io.BCM)

button_io_pin = 23
io.setup(button_io_pin, io.IN) # Specify that button_io_pin will be an input
button_previous_input = 0

while True:
    # Get the state of the button input
    button_input = io.input(button_io_pin)
    if (button_input != button_previous_input):
        # When the button changes state, print its value
        print button_input
        button_previous_input = button_input