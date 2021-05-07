### https://cdn-learn.adafruit.com/downloads/pdf/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi.pdf

import os
import time
import busio
import digitalio
import RPi.GPIO as GPIO
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# adding dig for photoresistor
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)
GPIO.setup(17, GPIO.IN)

#create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

#Create the chip select (cs)
cs = digitalio.DigitalInOut(board.D22)

#create the mcp object
mcp = MCP.MCP3008(spi, cs)

#create an analog input channel on pin 0
chan0 = AnalogIn(mcp,MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
chan2 = AnalogIn(mcp,MCP.P2)

print('Raw ADC value: ', chan0.value)
print('ADC Voltage: ', str(chan0.voltage)+'V')

while True:
	try:
		photosensor = chan0.value
		moisture = chan1.value
		temp = chan2.value
		print()
		print("ADC Photosensor Value: "+str(photosensor))
		#print("ADC Voltage: "+str(chan0.voltage)+"V")
		print("Photosensor: "
		R = 10
		places = 2
		volts = (photosensor * 3.3) / 1023
		volts = round(volts, places)
		print('volts = ', volts)
		if volts == 0:
		    lux = 0
		else:
		    lux = 500 * (3.3 - volts) / (R * volts)
		print('lux = ', lux)
		#print("Photosensor: "+str(photosensor/1023))
		#print("Digital GPIO: "+str(GPIO.input(27)))
		print()
		print("ADC Moistur Sens: "+str(moisture))
		#print("ADC Voltage: "+str(chan1.value))
		print("Moisture: "+str(moisture/1023))
		#print("Digital GPIO moist: "+str(GPIO.input(17)))
		print()
		print("ADC Temp Sens: " +str(temp))
		print("Temp: "+str(temp/1023))
		#print("ADC Voltage: "+str(chan2.value))
		time.sleep(20)
	except KeyboardInterrupt:
		GPIO.cleanup()
		exit()
