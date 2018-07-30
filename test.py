#!/usr/bin/env python3
import api.cloudmon
import os
import sys
import tests.php_build_speedtest
import tests.cpu_speedtest
import tests.file_speedtest
import tests.network_speedtest


def main():
    print('Welcome at the test !')
    print(sys.argv)
    test = sys.argv[1]
    if test == 'php':
        print(tests.php_build_speedtest.clone_php_src())
        print(tests.php_build_speedtest.perform_test())
    elif test == 'cpu':
        print(tests.cpu_speedtest.install_coremark())
        print(tests.cpu_speedtest.perform_test())
    elif test == 'file':
        print(tests.file_speedtest.install_fio())
        print(tests.file_speedtest.perform_test())
    elif test == 'network':
        print(tests.network_speedtest.perform_test())
    elif test == 'volume':
        print(tests.file_speedtest.install_fio())
        print(tests.file_speedtest.perform_test(True))


if __name__ == "__main__":
    main()
