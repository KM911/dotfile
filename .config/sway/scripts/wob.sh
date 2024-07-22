#!/bin/bash


if pgrep tail  > /dev/null ;
# if pgrep -f "footclient -a $1"  > /dev/null ;1
then
    echo "work"
    exit 0
else
    echo "not work"
    tail -f /tmp/wobpipe | wob &

fi
