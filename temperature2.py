import time
from w1thermsensor import W1ThermSensor
from ISStreamer.Streamer import Streamer

streamer = Streamer(bucket_name="Temperature Stream", bucket_key="piot_temp_stream031815", access_key="PUT_YOUR_ACCESS_KEY_HERE")

therm_sensor = W1ThermSensor()

def start_streaming():
	while True:
		temp_celcius = therm_sensor.get_temperature()
		streamer.log("temperature (C)", temp_celcius)
		temp_fahrenheit = therm_sensor.get_temperature(W1ThermSensor.DECREES_F)
		streamer.log("temperature (F)", temp_fahrenheit)
		time.sleep(.5)
		streamer.flush()

def stop_streaming():
	streamer.close()


if __name_ == "__main__":
	try:
		print("starting temp streamer")
		start_streaming()
	except KeyboardInterrupt:
		print("stopping temp streamer")
		stop_streaming()