import os
import time
import json
from subprocess import call


def install_coremark():
    call(['git', 'clone', 'https://github.com/cloud-mon/coremark.git'])


def perform_test():
    fileName = "coremark/tmp_result.json"
    try:
        os.remove(fileName)
    except OSError:
        pass
    print(call(
        'coremark/make PORT_DIR=linux64 ITERATIONS=200000 XCFLAGS="-g -O2 -DMULTITHREAD=2 -DUSE_PTHREAD -DPERFORMANCE_RUN=1" REBUILD=1',
        shell=True))
    f = open(fileName, "r+")
    print(f.read())

