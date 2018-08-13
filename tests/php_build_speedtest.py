import os
import time
import json
from subprocess import call


def clone_php_src():
    call(['git', 'clone', 'https://github.com/php/php-src.git'])


def perform_test():
    file_name = "php-src/test_result.log"
    sec_start = time.time()
    try:
        os.remove(file_name)
    except OSError:
        pass
    call('cd php-src && ./buildconf -f >> /dev/null && ./configure >> /dev/null ',
         shell=True)
    command = 'cd php-src && time make -s -j ' + str(os.getenv(
        'SERVER_CORES', '1'))
    print(command)
    call(command, shell=True)
    sec_end = time.time()
    return round(sec_end - sec_start, 2)
