#!/bin/bash

# 1 start suck



# pgrep 
if pgrep  wezterm-gui > /dev/null ;
then
    # echo "st is alive"
    # swaymsg scratchpad [app_id="org.wezfurlong.wezterm"] show
    
    # swaymsg scratchpad show
    # swaymsg "[app_id=\"org.wezfurlong.wezterm\"] move to scratchpad"
    # swaymsg scratchpad show
else
    # echo "st is not alive"
    wezterm-gui  &
    sleep 0.5
    # swaymsg move [app_id="org.wezfurlong.wezterm"] to scratchpad
    # 
    swaymsg move to scratchpad
    swaymsg "[app_id=\"org.wezfurlong.wezterm\"] scratchpad show"
fi
# $bindsym $mod+p             exec ~/.config/sway/scripts/suckless.sh f1, exec 'swaymsg [app_id="f1"] scratchpad show' , exec "waybar-signal scratchpad"

#     swaymsg "[app_id=\"org.wezfurlong.wezterm\"] move to scratchpad"

# toogle