#!/bin/bash

if [ "$(whoami)" != "root" ]
then
    sudo su -s "$0"
    exit
fi

echo mmc0 > /sys/class/leds/led0/trigger

echo "
Onboard LED will now return to system control"