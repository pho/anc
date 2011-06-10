#!/bin/python

#Author: pho <phofin@gmail.com>

# Fast python code for use a NES Controller with an Arduino
# Reads from serial port a string with the states
# 0 = Pushed

#Requeriments:
# X
# python-xlib

#Usage example:
# python scan.py /dev/ttyUSB0

#Config
# A B SELECT START UP DOWN LEFT RIGHT

#Why are the default config set to Control/Alt/Super?
#Because of the autorepeat delay, it's dificult to play anything
#it the key do some delay. The keypresses are sent to the X, so is an
#system config issue. If you know how to do this better, contact me ;D

but = ["Alt_L", "Control_R", "f", "g", "Super_L", "Super_R", "Shift_R", "Shift_L"]

delay = 0.1 #Scan might be too fast

import serial, os, sys, signal
from Xlib import X, XK  
from Xlib.display import Display  
from Xlib.ext import xtest  
from time import sleep

if len(sys.argv) < 2:
  print "(1) Argument needed"
  print "Usage: scan.py /dev/ttyUSB0"
  sys.exit(-1)

#catch ctrl+c
def signal_handler(signal, frame):
    print "exiting..."
    d.flush()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

d = Display()  

#Transform the keys strings to keycodes
for i in range(0, len(but)):  
    but[i] = d.keysym_to_keycode(XK.string_to_keysym(but[i]))  

ser = serial.Serial(sys.argv[1], 9600)

while 1:
  ser.write('a');
  
  try:
    actual = ser.read()
    while (actual == -1):
      actual = ser.read()
    actual += ser.readline()
  except:
    print "Something is wrong. Restarting..."
    ser.close()
    ser = serial.Serial(sys.argv[1], 9600)
  if len(actual) != 9:
    continue #Bad

  for i in range(0, 8):
    if list(actual)[i] == '0':
      xtest.fake_input(d, X.KeyPress, but[i])  
      d.sync()
      d.flush()
    else:
      xtest.fake_input(d, X.KeyRelease, but[i])  
      d.sync() 
      d.flush()
      
  sleep(delay)
