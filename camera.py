#!/usr/bin/python


# Import required modules
import picamera
import time
import signal
import sys
import os


# The following code will write the Process ID of this script to a hidden file
pid = os.getpid()
PIDfilename = ".PID"
PIDfile = open(PIDfilename, "wt")
PIDfile.write(str(pid))
PIDfile.close()


# Variables
numpics = 5
numburst = 5
rectime = 300


# Functions

def capture(numPics):
	for i in range(0,numPics):
		picname = str(time.strftime('%I%M%S%p_%d-%m-%y'))
		camera.capture('Pictures/' + picname + '.jpg')
		time.sleep(1)

def burst(numBurst):
	camera.capture_sequence([ 'Pictures/' + str(time.strftime('%I%M%S%p_%d-%m-%y')) + '_burst' + str(i+1) + '.jpg' for i in range(numBurst) ])

def record(recTime):
	vidname = str(time.strftime('%I%M%S%p_%d-%m-%y'))
	camera.start_recording('Videos/' + vidname + '.h264')
	time.sleep(recTime)
	camera.stop_recording()
	time.sleep(1)

def signal_term_handler(signal, frame):
	camera.close()
	os.remove(PIDfilename) 		#removes the hidden temp PID file
	sys.exit()


signal.signal(signal.SIGTERM, signal_term_handler)


try:
	with picamera.PiCamera() as camera:
		while True:
			camera.start_preview(alpha=0)
			time.sleep(2)
			capture(numpics)
			burst(numburst)
			record(rectime)
			camera.stop_preview()
			time.sleep(2)


except KeyboardInterrupt:
	camera.close()
	os.remove(PIDfilename) 		#removes the hidden temp PID file
	sys.exit()