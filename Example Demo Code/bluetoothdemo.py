#bluetooth code - test commit


## Original from https://circuitdigest.com/microcontroller-projects/controlling-raspberry-pi-gpio-using-android-app-over-bluetooth

import bluetooth
import RPi.GPIO as GPIO
# LED at this GPIO Pin
LED=21

# BCM PIN numbers 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Init output Pin
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,0)

# Bluetooth open socket
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_socket.bind(("",port))
server_socket.listen(1)

# Connection from BlueTerm app yields this message
client_socket,address= server_socket.accept()
print("Accepted connection from ", address)
# Do check with app
while 1:
	data = client_socket.recv(1024)
	print("Received: %s" % data)
	#print(data) #test print
	
	#LED OFF
	if (data== b'0'):
		print("GPIO 21 LOW,LED OFF")
		GPIO.output(LED,0)
	# LED ON
	if(data==b'1'):
		print("GPIO 21 HIGH, LED ON")
		GPIO.output(LED,1)
	# Break Loop - some issue with BlueTerm when sending this from phone app
	if(data==b'q'):
		GPIO.output(LED,0)
		print("Quit")
		break

# Close sockets before ending program
client_socket.close()
server_socket.close()
