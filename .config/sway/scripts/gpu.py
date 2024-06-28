#!/usr/bin/python

import subprocess


def get_device_temp(src: str) -> str:
    text = subprocess.run(
        ["cat", src], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
    if text == "":
        print("GPU")
    else:
        print(text.strip("000"))


amd_gpu = "/sys/class/hwmon/hwmon6/temp1_input"

get_device_temp(amd_gpu)
