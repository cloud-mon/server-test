import os
import time
import json
from subprocess import call


def clone_php_src():
    if os.path.isdir("ovs"):
        call(['rm','-rf', 'ovs'])
    call(['git', 'clone', '--depth', '1','https://github.com/openvswitch/ovs.git', '-b' 'branch-3.1'])


def perform_test():
    file_name = "ovs/test_result.log"
    try:
        os.remove(file_name)
    except OSError:
        pass
    call('cd ovs && git checkout origin/branch-3.1 && ./boot.sh >> /dev/null && ./configure >> /dev/null',
         shell=True)
    command = 'cd ovs && time make -s -j $(nproc)'
    print(command)
    sec_start = time.time()
    call(command, shell=True)
    sec_end = time.time()
    return round(sec_end - sec_start, 2)
