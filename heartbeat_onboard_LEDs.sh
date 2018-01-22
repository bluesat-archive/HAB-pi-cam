#!/bin/bash

if [ "$(whoami)" != "root" ]
then
    sudo su -s "$0"
    exit
fi

echo heartbeat > /sys/class/leds/led0/trigger

echo "
Onboard LED will now be flashing"