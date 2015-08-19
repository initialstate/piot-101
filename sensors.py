import os
import glob
import time
import RPi.GPIO as io
import thread
from ISStreamer.Streamer import Streamer

# --------- User Settings ---------
BUCKET_NAME = ":computer: Sensors"
BUCKET_KEY = "piot_sensor_stream082315"
ACCESS_KEY = "PUT_YOUR_ACCESS_KEY_HERE"
TEMPERATURE_TOO_HIGH_F = 85
TEMPERATURE_TOO_LOW_F = 50
# ---------------------------------

io.setmode(io.BCM)
door_pin = 23
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

def stream_temp(streamer):
    while True:
        temp_c = read_temp()
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        if temp_f > TEMPERATURE_TOO_HIGH_F:
            streamer.log("Status", ":fire:")
        elif temp_f < TEMPERATURE_TOO_LOW_F:
            streamer.log("Status", ":snowflake:")
        else:
            streamer.log("Status", ":thumbsup:")
        streamer.log("temperature (C)", temp_c)
        streamer.log("temperature (F)", temp_f)
        print "Temperature: " + str(temp_f) + " F"
        streamer.flush()
        time.sleep(.5)

def main():
    streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
    # Start temperature stream thread
    try:
       thread.start_new_thread(stream_temp, (streamer, ))
    except:
       print "Error: unable to start temperature streamer thread"

    # Door sensor
    door_status = 1
    while True:
        ## if the switch is open
        if (io.input(door_pin) == True and door_status != 0):
            streamer.log(":door: Door", "Open") 
            print "Door Open"
            streamer.flush() 
            door_status = 0 
        ## if the switch is closed 
        if (io.input(door_pin) == False and door_status != 1):
            streamer.log(":door: Door", "Close") 
            print "Door Closed"
            streamer.flush() 
            door_status = 1 
        time.sleep(2)

if __name__ == "__main__":
    main()            
