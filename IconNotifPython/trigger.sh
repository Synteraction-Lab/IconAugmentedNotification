#!/bin/bash

#sudo sync
#sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches'

#if pgrep -x "vlc" > /dev/null
#then
#    echo "VLC running"
#else
#    echo "VLC starting"
#    vlc > /dev/null 2>&1 &
#fi

#conda init bash
#conda activate psychopy
python task_vigilance.py