#!/bin/bash 





if pgrep -f $1  > /dev/null ;
# if pgrep -f "footclient -a $1"  > /dev/null ;1
then
    exit 0
else
    $1
fi



