#!/bin/bash

python camera.py &
echo "Started recording...
"
echo "Process number: $!"
./heartbeat_onboard_LEDs.sh