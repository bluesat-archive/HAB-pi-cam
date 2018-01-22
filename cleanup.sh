#!/bin/bash


if [ -f ".PID" ]
then
	echo "Recording script is running. Please stop this first by running ./kill.sh"
	exit 1
fi


echo "
Do you wish to delete all media? 
Enter Option No. and hit enter.
WARNING: THIS CANNOT BE UNDONE!
"
select yn in "Yes" "No" "Cancel"; do
    case $yn in
        Yes )
		cd Pictures
		rm -f *.jpg
		cd ../Videos
		rm -f *.h264
		echo "
Removed all media"
		exit 1;;
        No )
		echo "
Did not remove anything"
		exit 1;;
	Cancel )
		echo "
Cancelled"
		exit 1;;
	*)
		echo "Invalid Option";;
    esac
done
