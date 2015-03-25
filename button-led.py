# Import library that lets you control the Pi's GPIO pins
import RPi.GPIO as io 
# Import time for delays 
from time import sleep

# Disables messages about GPIO pins already being in use
io.setwarnings(False)
# Numbering scheme that corresponds to breakout board and pin layout
io.setmode(io.BCM)

led_io_pin = 4
button_io_pin = 23
# Specifies that led_pin will be an output
io.setup(led_pin, io.OUT)
# Specifies that button_io_pin will be an input
io.setup(button_io_pin, io.IN)

button_on = False
previous_button_input = 0

while True:
    # Get the state of the button input
    button_input = io.input(button_io_pin)
    # Debounce the button
    if ((not prev_input) and button_input):
        # Toggle the button on and off
        button_on = not button_on
    prev_input = button_input
    sleep(0.05)
    
    if button_on:
        # Turn the LED on
        io.output(led_pin, io.HIGH)
    else:
        # Turn the LED off
        io.output(led_pin, io.LOW)