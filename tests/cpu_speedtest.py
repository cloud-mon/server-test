import os
import time
import json
from subprocess import call


def install_coremark():
    if os.path.isdir("coremark"):
        call(['rm','-rf', 'coremark'])

    call(['git', 'clone', 'https://github.com/cloud-mon/coremark.git'])


def perform_test():
    file_name = "coremark/run1.log"
    try:
        os.remove(file_name)
    except OSError:
        pass
    print(call(
        'cd coremark && make PORT_DIR=linux64 XCFLAGS="-g -O2 -DMULTITHREAD=`nproc` -DUSE_PTHREAD -DPERFORMANCE_RUN=1" REBUILD=1 >> /dev/null',
        shell=True))
    f = open(file_name, "r+")
    data = f.read()

    return parse_result(data)


def parse_result(result=None):
    parsed_result = {
        'iterations_per_sec': 0,
    }
    data = result.replace('2K performance run parameters for coremark.', '').replace(' ', '').splitlines()
    for line in data:
        if len(line) > 0:
            _data = line.split(':')
            if _data[0] == 'Iterations/Sec':
                parsed_result['iterations_per_sec'] = _data[1]

    return parsed_result
