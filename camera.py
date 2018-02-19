#!/usr/bin/python2


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
numpics = 5			# number of still pictures taken
numburst = 5		# number of burst pictures taken
rectime = 300		# length of time to record in each loop between pictures (in seconds)


# Functions
# This function will take a number of still pictures, as defined by the input parameter
def capture(numPics):
	for i in range(0,numPics):
		picname = str(time.strftime('%I%M%S%p_%d-%m-%y'))
		camera.capture('Pictures/' + picname + '.jpg')
		time.sleep(1)

# This function will take a burst of pictures
def burst(numBurst):
	camera.capture_sequence([ 'Pictures/' + str(time.strftime('%I%M%S%p_%d-%m-%y')) + '_burst' + str(i+1) + '.jpg' for i in range(numBurst) ])

def record(recTime):
	vidname = str(time.strftime('%I%M%S%p_%d-%m-%y'))
	camera.start_recording('Videos/' + vidname + '.h264')
	time.sleep(recTime)
	camera.stop_recording()
	time.sleep(1)

# The following function handles the case when a kill signal is sent to the process
def signal_term_handler(signal, frame):
	camera.close()
	os.remove(PIDfilename) 		#removes the hidden temp PID file
	sys.exit()

signal.signal(signal.SIGTERM, signal_term_handler)


try:
	with picamera.PiCamera() as camera:
		while True:
			camera.start_preview(alpha=0)		#starting the preview "warms up" the camera, and is recommended in the PiCamera documentation
			time.sleep(2)
			capture(numpics)
			burst(numburst)
			record(rectime)
			camera.stop_preview()
			time.sleep(2)


# Handles the case when user exits the running script using Control+C
except KeyboardInterrupt:
	camera.close()
	os.remove(PIDfilename) 		#removes the hidden temp PID file
	sys.exit()
