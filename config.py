#!/usr/bin/env python3
import os

import sys


Configs = ["sway", "waybar", "nushell", "helix", "rofi", "yazi"]

Etcs = ["/etc/environment", "~/.cargo/config.toml"]


Scripts = [
    "/usr/bin/pp",
    "/usr/bin/time"
]


def ListToDict(x):
    Dict = {}
    for i in x:
        filename = i.split("/")[-1]
        Dict[filename] = i
    return Dict


EtcDict = ListToDict(Etcs)
ScriptsDict = ListToDict(Scripts)


def hard_link(dc: dict, fd: str, is_back=True):
    if is_back is True:
        for p, v in dc.items():
            print(f"sudo cp -r -l {v} ./{fd}/{p}")
            os.system(f"sudo cp -r -l {v} ./{fd}/{p}")
    else:
        for p, v in dc.items():
            print(f"sudo cp -r -l ./{fd}/{p} {v}")
            os.system(f"sudo cp -r -l ./{fd}/{p} {v}")


def config_back():
    for i in Configs:
        os.system(f"sudo cp -r -l ~/.config/{i} ./.config")


def config_restore():
    os.system(f"sudo cp - r - l ./.config/* ~/.config")


def etc_back():
    hard_link(EtcDict, "etc")


def etc_restore():
    hard_link(EtcDict, "etc", is_back=False)


def script_back():
    hard_link(ScriptsDict, "script")


def script_restore():
    hard_link(ScriptsDict, "script", is_back=False)


# back
def back():
    config_back()
    etc_back()
    script_back()

# restore


def restore():
    config_restore()
    etc_restore()
    script_restore()


script_restore()
