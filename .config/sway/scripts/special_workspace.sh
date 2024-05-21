#!/bin/bash 

app=$1
if pgrep -f $app > /dev/null ;
then
    # echo "st is alive"
    swaymsg scratchpad show
else
    # echo "st is not alive"
    $app  &
    sleep 0.05
    swaymsg move scratchpad
    swaymsg scratchpad show
fi