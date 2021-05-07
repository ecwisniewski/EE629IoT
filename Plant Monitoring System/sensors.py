import os
import sys
import time
import Adafruit_DHT
import busio
import digitalio
#import RPi.GPIO as GPIO
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

import MySQLdb


# Connect to Database
db = MySQLdb.connect("localhost", "pi","password", "database")
cursor=db.cursor()


# adding dig for photoresistor
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(27, GPIO.IN)
#GPIO.setup(17, GPIO.IN)

#create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

#Create the chip select (cs)
cs = digitalio.DigitalInOut(board.D22)

#create the mcp object
mcp = MCP.MCP3008(spi, cs)

#create an analog input channel on pins (0 and 1)
chan0 = AnalogIn(mcp,MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
#chan2 = AnalogIn(mcp,MCP.P2)

#print('Raw ADC value: ', chan0.value)
#print('ADC Voltage: ', str(chan0.voltage)+'V')

while True:
	try:
		# Humidity and Temperature Digital Sensor
		humidity, temperature = Adafruit_DHT.read_retry(11,4)
		temp_c = float(temperature)
		# Get Temperature
		temp_f = temp_c * 9.0 / 5.0 + 32.0

		# Get Analog values SPI
		photosensor = chan0.value
		moisture = chan1.value
		#temp = chan2.value
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
		#print("ADC Temp Sens: " +str(temp))
		#print("Temp: "+str(temp/1023))
		#print("ADC Voltage: "+str(chan2.value))
		print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))
		print('Temp: {0:0.1f} C, Temp F {1: 0.1f} F'.format(temp_c, temp_f))

		cursor.execute("INSERT INTO plantinfotest values(CURRENT_DATE(), NOW(), {0:0.1f}, {1:0.1f}, {2:0.1f}, {3:0.1f})".format(moisture,lux,temp_f,humidity))
		time.sleep(20)
	except KeyboardInterrupt:
		GPIO.cleanup()
		exit()
