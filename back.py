#!/usr/bin/env python3
from rich import print
from rich.prompt import Confirm, Prompt
import os

import sys
from config import *


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
        print(f"sudo cp -r -l ~/.config/{i} ./.config")
        os.system(f"sudo cp -r -l ~/.config/{i} ./.config")


def config_restore():
    print("sudo cp - r - l ./.config/* ~/.config")
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


# script_back()
# back()
# script_restore()


def docker_proxy():
    import json
    file = open('/etc/docker/daemon.json', 'r')
    data = json.load(file)
    file.close()

    if 'registry-mirrors' not in data:
        data['registry-mirrors'] = [
            "https://hub-mirror.c.163.com",
            "https://mirror.baidubce.com"
        ]
        file = open('/etc/docker/daemon.json', 'w')
        json.dump(data, file, indent=4)
        file.close()

# write a reactive command line


options = ["back", "restore"]
optionss = [1, 2]
try:
    for option in options:
        print(option)
    #
    choice = Prompt.ask("请选择一个选项")

    # print("choice ", choice)
    # if choice:
    print(f"你选择了: {options[int(choice)-1]}")  # 这里可以根据实际选择情况进行处理
    if options[int(choice)-1] == "back":
        back()
    elif options[int(choice)-1] == "restore":
        restore()
    else:
        print("exit")
        sys.exit(0)
except KeyboardInterrupt:
    # print("exit")
    sys.exit(0)
