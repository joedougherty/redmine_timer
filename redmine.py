import serial
import time
import sys
import datetime

ser = serial.Serial('/dev/ttyACM0', 9600)
ticket_num = str(input("Enter Redmine ticket #:"))

while 1:
	serialMsg = ser.readline()

	if serialMsg == 'on\r\n':
		print "Tracking time on ticket #" + ticket_num
		start_time = time.time()

	if serialMsg == 'off\r\n':
		elapsed_time = time.time() - start_time
		# Convert time spent to hours
		# Get time spent on ticket so far from Redmine API
		# Add existing spent time to calculated spent time and update the ticket
		sys.exit(0)
