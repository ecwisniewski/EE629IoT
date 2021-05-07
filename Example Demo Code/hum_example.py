import sys
import Adafruit_DHT
import time

while True:
	try:
		humidity, temperature = Adafruit_DHT.read_retry(11,4)
		temp_c = float(temperature)
		temp_f = temp_c * 9.0 / 5.0 + 32.0

		print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))
		print('Temp: {0:0.1f} C, Temp F {1: 0.1f} F'.format(temp_c, temp_f))
		time.sleep(3)
	except KeyboardInterrupt:
		exit()
