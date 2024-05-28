#!/bin/bash 


if pgrep -f /opt/spotify/spotify > /dev/null ;
then
    # echo "st is alive"
    # swaymsg scratchpad show
    exit 0
else
    # echo "st is not alive"
    /usr/bin/spotify &
    sleep 1
    swaymsg move scratchpad
    # swaymsg scratchpad show
fi