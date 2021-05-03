## Code from IoT example

import RPi.GPIO as GPIO
import time
import spidev

#moisture sensor channel
moisture_channel=1

GPIO.setmode(GPIO.BCM)
TRIGGER_PIN =22
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
threshold=100

#Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 976000

#Function read SPI data from MCP3008 chip
def ReadChannel(channel):
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1] & 3) << 8) + adc[2]
	return data

# Function to read sensor connected
def readMoisture():
	level = 1023-ReadChannel(moisture_channel)
	return level

# Controller main function
def runController():
	level = readMoisture()

#If the moisture level is lower/higher than the threshold, turn on/off actuators
	if (level < threshold):
		GPIO.output(TRIGGER_PIN, True)
	else:
		GPIO.output(TRIGGER_PIN, False)

	print("Moisture: %s" % level)

while True:
	try:
		runController()
		time.sleep(5)
	except KeyboardInterrupt:
		GPIO.cleanup()
		exit()
