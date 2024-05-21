#!/bin/bash

# 1 start suck



# pgrep 
if pgrep -f footclient > /dev/null ;
then
    # echo "st is alive"
    swaymsg scratchpad show
else
    # echo "st is not alive"
    footclient  &
    sleep 0.05
    swaymsg move scratchpad
    swaymsg scratchpad show
fi