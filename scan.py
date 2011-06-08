#!/bin/python

#Author: pho <phofin@gmail.com>

# Fast python code for use a NES Controller with an Arduino
# Reads from serial port a string with the states
# 0 = Pushed

#Requeriments:
# xte


#Config
# A B SELECT START UP DOWN LEFT RIGHT
but = ["a", "b", "Shift_R", "Return", "Up", "Down", "Left", "Right"]
delay = 0.0 #Scan might be too fast

import serial, os, sys, signal
from time import sleep

#catch ctrl+c
def signal_handler(signal, frame):
		print "exiting..."
		sys.exit(0)
		
signal.signal(signal.SIGINT, signal_handler)

ser = serial.Serial("/dev/ttyUSB1", 9600)

while 1:
	ser.write('a');
	
	actual = ser.read()
	while (actual == -1):
		actual = ser.read()
	actual += ser.readline()

	if len(actual) != 9:
		continue #Bad

	for i in range(0, 8):
		if list(actual)[i] == '0':
			os.system("xte \"keydown " + but[i] + "\"")
		else:
			os.system("xte \"keyup " + but[i] + "\"")
	sleep(delay)
