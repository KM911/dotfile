#!/bin/bash

# 1 start suck



# pgrep 
if pgrep  wezterm > /dev/null ;
then
    # echo "st is alive"
    # swaymsg scratchpad [app_id="org.wezfurlong.wezterm"] show
    swaymsg scratchpad show

else
    # echo "st is not alive"
    wezterm-gui  &
    sleep 0.5
    # swaymsg move [app_id="org.wezfurlong.wezterm"] to scratchpad
    # swaymsg scratchpad [app_id="org.wezfurlong.wezterm"] show
    swaymsg move to scratchpad
    # swaymsg scratchpad show
fi