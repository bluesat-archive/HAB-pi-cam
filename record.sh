#!/bin/bash

file=".PID"

if [ -f "$file" ]
then
	echo "Recording script is already running. You can stop it by typing ./kill.sh"
	exit 1
fi

python camera.py &
echo "Started recording...
"
echo "Process number: $!"
./heartbeat_onboard_LEDs.sh
