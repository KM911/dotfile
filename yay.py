#!/usr/bin/env python3
import sys
import os
from config import *


def install():
    for image in images:
        os.system(f"docker pull {image}")

    for pkg in total:
        os.system(f"yay -S --noconfirm {pkg}")


install()
