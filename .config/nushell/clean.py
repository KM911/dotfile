#!/usr/bin/python


file = open("/home/km/.config/nushell/history.txt", "r")
lines = file.readlines()
file.close()

file = open("/home/km/.config/nushell/history.txt", "w+")
new_lines = list(set(lines))
file.writelines(new_lines)
file.close()
