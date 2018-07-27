#!/usr/bin/env python3
import api.cloudmon
import os
import sys
import tests.php_build_speedtest
import tests.cpu_speedtest


def main():
    print('Welcome at the test !')
    print(sys.argv)
    # tests.php_build_speedtest.clone_php_src()
    # tests.php_build_speedtest.perform_test()
    print(tests.cpu_speedtest.install_coremark())
    print(tests.cpu_speedtest.perform_test())


if __name__ == "__main__":
    main()
