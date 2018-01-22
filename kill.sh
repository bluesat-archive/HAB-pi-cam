#!/bin/bash

file=".PID"

if [ -f "$file" ]
then
	echo "Stopping recording process, please wait a moment..."
else 
	"Recording has not been started, please start it with ./record.sh"
	./stop_LEDs.sh
	exit 1
fi

read -r PID<$file
kill $PID
echo "$PID was killed"

echo "
Recording successfully stopped."

./stop_LEDs.sh