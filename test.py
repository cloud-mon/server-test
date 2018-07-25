#!/usr/bin/env python3
import api.cloudmon
import os
import sys
import tests.cpu_speedtest
import tests.network_speedtest


def main():
    print('Welcome at the test !')
    print(sys.argv)
   # tests.cpu_speedtest.install_coremark()
    tests.cpu_speedtest.perform_test()


if __name__ == "__main__":
    main()
