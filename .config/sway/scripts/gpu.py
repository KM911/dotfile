#!/usr/bin/python

import subprocess

text = subprocess.run(["cat", "/sys/class/hwmon/hwmon6/temp1_input"],
                      stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

print(text.strip("000"))

# text =
