#!/bin/bash

# 1 start suck



# pgrep 
if pgrep -f footclient  > /dev/null ;
then
    exit 0
else
    footclient  &
    sleep 0.1
    swaymsg move to scratchpad
    swaymsg "[app_id=\"footclient\"] scratchpad show"
fi













