#Import library that lets you control the Pi's GPIO pins
import RPi.GPIO as io

# Disable messages about GPIO pins already being in use
io.setwarnings(False)
# Numbering scheme that corresponds to breakout board and pin layout 
io.setmode(io.BCM)

pinNumBTN = 23
io.setup(pinNumBTN, io.IN) # Specify that pinNumBTN will be an input prevInput = 0

while True:
    # Get the state of the button input
    btnInput = io.input(pinNumBTN)
    if (btnInput != prevInput):
        # When the button changes state, print its value
        print btnInput
        prevInput = btnInput
