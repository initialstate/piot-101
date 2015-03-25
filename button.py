#Import library that lets you control the Pi's GPIO pins
import RPi.GPIO as GPIO

# Disable messages about GPIO pins already being in use
GPIO.setwarnings(False)
# Numbering scheme that corresponds to breakout board and pin layout 
GPIO.setmode(GPIO.BCM)

pinNumBTN = 23
GPIO.setup(pinNumBTN,GPIO.IN) # Specify that pinNumBTN will be an input prevInput = 0

while True:
    # Get the state of the button input
    btnInput = GPIO.input(pinNumBTN)
    if (btnInput != prevInput):
        # When the button changes state, print its value
        print btnInput
        prevInput = btnInput