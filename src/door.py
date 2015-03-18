import time # so we can use "sleep" to wait between actions
import RPi.GPIO as io # import the GPIO library we just installed but call it "io"
from ISStreamer.Streamer import Streamer # import the ISStreamer

## name the bucket and individual access_key
streamer = Streamer(bucket_name="Locker Protector", bucket_key="locker_protector", access_key="YOUR_ACCESS_KEY_HERE")

is.setmode(io.BCM) # set GPIO mode to BCM
door_pin = 23 # enter the number of whatever GPIO pin your're using
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP) # use the built-in pull-up resistor

door=0 # initialize door

## Event loop
while True:
    ## if the switch is open
    if io.input(door_pin):
        streamer.log("Door", "Open") # stream a message saying "Open"
        streamer.flush() # send the message immediately
        print "Open"
        door=0 # set door to its initial value
        time.sleep(1) # wait 1 second before the next action
    ## if the switch is closed and door does not equal 1
    if (io.input(door_pin) == False and door != 1):
        streamer.log("Door", "Close") # stream a message saying "Close"
        streamer.flush() # send the message immediately
        print "Close"
        door=1 # set door so that this loop won't act again until the switch has been opened