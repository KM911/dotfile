#!/usr/bin/python

import subprocess


def get_device_temp(src: str) -> str:
    # get subprocess exit_code
    process = subprocess.run(
        ["bluetoothctl", "info"], stdout=subprocess.PIPE)
    text = process.stdout.decode('utf-8').strip()
    exit_code = process.returncode
    # print(exit_code)
    # print(text)
    # if text == "":
    #     print("GPU")
    # else:
    #     print(text.strip("000"))
    if exit_code == 0:
        # parser the blue info
        print(text[-3:-1], end="%")
    else:
        print("")


amd_gpu = "/sys/class/hwmon/hwmon6/temp1_input"

get_device_temp(amd_gpu)
