### Plant Monitor - Get Values from Sensors and Input into Database Table
import os
import sys
import time
import Adafruit_DHT
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

import MySQLdb


# Connect to Database
db = MySQLdb.connect("localhost", "pi","password", "database")
cursor=db.cursor()

#create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

#Create the chip select (cs)
cs = digitalio.DigitalInOut(board.D22)

#create the mcp object
mcp = MCP.MCP3008(spi, cs)

#create an analog input channel on pins (0 and 1)
chan0 = AnalogIn(mcp,MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)

# Read Sensors 
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
		
		#Print ADC Values
		print()
		print("ADC Photosensor Value: "+str(photosensor))
		
		photo = photosensor/1023
		print("Photosensor: "+str(photo))
		
		print()
		print("ADC Moistur Sens: "+str(moisture))
		moist = moisture/1023
		print("Moisture: "+str(moist))
		
		print()

		print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))
		print('Temp: {0:0.1f} C, Temp F {1: 0.1f} F'.format(temp_c, temp_f))
		try:
			cursor.execute("INSERT INTO plantinfotest values(CURRENT_DATE(), NOW(), {0:0.1f}, {1:0.1f}, {2:0.1f}, {3:0.1f})".format(moist,photo,temp_f,humidity))
			db.commit()
			print("Data committed")
		except:
			print("Error: the database is being rolled back")
			db.rollback()
 
		time.sleep(20)
	except KeyboardInterrupt:
		print("Program Interrupted")
		cursor.execute ("SELECT * FROM plantinfotest")
		print("\nDATE		TIME		MOISTURE	LIGHT   TEMPERATURE   HUMIDITY")
		print("==========================================================================")
		for reading in cursor.fetchall():
			print(str(reading[0])+"	"+str(reading[1])+"	"+str(reading[2])+"		"+str(reading[3])+"	  "+str(reading[4])+"		"+str(reading[5]))

		db.close()
		exit()

