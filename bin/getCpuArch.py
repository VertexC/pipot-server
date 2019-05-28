#!/usr/bin/env python
import sys
import subprocess
import os


def getArch():
    info = subprocess.check_output(["lscpu"]).decode("utf-8")
    # print(info)
    arch = info.split('\n')[0].split()[1]
    return arch


if __name__ == "__main__":
    sys.stdout.write("%s\n" % getArch())
