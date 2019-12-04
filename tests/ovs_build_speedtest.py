import os
import time
import json
from subprocess import call


def clone_php_src():
    call(['git', 'clone', '--depth', '1','https://github.com/php/php-src.git', '-b' 'branch-2.7'])


def perform_test():
    file_name = "ovs/test_result.log"
    try:
        os.remove(file_name)
    except OSError:
        pass
    call('cd ovs && git checkout origin/branch-2.7 && ./boot.sh && ./configure',
         shell=True)
    command = 'cdovsc && time make -s -j ' + str(os.getenv(
        'SERVER_CORES', '1'))
    print(command)
    sec_start = time.time()
    call(command, shell=True)
    sec_end = time.time()
    return round(sec_end - sec_start, 2)
