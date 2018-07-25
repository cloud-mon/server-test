import os
import time
import json
from subprocess import call


def clone_php_src():
    call(['git', 'clone', 'https://github.com/php/php-src.git'])


def perform_test():
    file_name = "php-src/test_result.log"
    try:
        os.remove(file_name)
    except OSError:
        pass
    print(call(
        'cd php-src && ./buildconf -f >> /dev/null && ./configure >> /dev/null ',
        shell=True))
    print(call(
        'cd php-src && time make -j ' + str(os.getenv(
            'SERVER_CORES', '1')) + '>> test_result.log ',
        shell=True))
    f = open(file_name, "r+")
    data = f.read()
    print(data)


# return parse_result(data)


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
