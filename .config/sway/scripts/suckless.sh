#!/bin/bash

# 1 start suck



if pgrep -f "foot" > /dev/null ;
then
    echo "start foot server"
else
    foot --server &> /dev/null &
fi




if pgrep -f "footclient -a $1"  > /dev/null ;
# if pgrep -f "footclient -a $1"  > /dev/null ;1
then
    exit 0
else
    footclient -a $1 &
    # footclient -a $1 -c ~/.config/foot/$1.ini &
    sleep 0.1
    swaymsg move to scratchpad
    swaymsg "[app_id=\"$1\"] scratchpad show"
fi