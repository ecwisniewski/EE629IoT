### https://cdn-learn.adafruit.com/downloads/pdf/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi.pdf

import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as mcp3008
from adafruit_mcp3xxx.analog_in import AnalogIn

#create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

#Create the chip select (cs)
cs = digitalio.DigitalInOut(board.D22)

#create the mcp object
mcp = MCP.MCP3008(spi, cs)

#create an analog input channel on pin 0
chan0 = AnalogIn(mcp,MCP.P0)

print('Raw ADC value: ', chan0.value)
print('ADC Voltage: ', str(chan0.voltage)+'V')

while True:
    print("ADC Value: "+str(chan0.value))
    time.sleep(0.5)
