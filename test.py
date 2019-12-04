#!/usr/bin/env python3
import api.cloudmon
import os
import sys
import tests.php_build_speedtest
import tests.ovs_build_speedtest
import tests.cpu_speedtest
import tests.file_speedtest
import tests.network_speedtest


def main():
    print('Cloud Mon on host tester!\n')
    if len(sys.argv) > 1:
        test = sys.argv[1]
        if test == 'php':
            print("Running PHP build Test\n")
            print(tests.php_build_speedtest.clone_php_src())
            print(tests.php_build_speedtest.perform_test())
        elif test == 'ovs':
            print("Running OVS build Test\n")
            print(tests.ovs_build_speedtest.clone_php_src())
            print(tests.ovs_build_speedtest.perform_test())
        elif test == 'cpu':
            print("Running CPU Test\n")
            print(tests.cpu_speedtest.install_coremark())
            print(tests.cpu_speedtest.perform_test())
        elif test == 'file':
            print("Running Filesystem Test\n")
            print(tests.file_speedtest.install_fio())
            print(tests.file_speedtest.perform_test())
        elif test == 'network':
            print("Running Network Test\n")
            print(tests.network_speedtest.perform_test())
        elif test == 'volume':
            print("Running Volume  Test\n")
            print(tests.file_speedtest.install_fio())
            print(tests.file_speedtest.perform_test(True))
    else:
        print("Help\n")
        print("Append one of the following arguments to perform the tests\n")
        print("php - performs a php build on the machine\n")
        print("ovs - performs a php build on the machine\n")
        print("cpu - performs a cpu benchmark based on coremark on the machine\n")
        print("file - performs a filesystem benchmark based on FIO on the machine\n")
        print("network - performs a network speedtest based on speedtest-cli on the machine\n")
        print("volume - performs a filesystem benchmark based on FIO on the volume attached to the machine.\n\t Need "
              "to be mounted under /mnt/test_volume\n")


if __name__ == "__main__":
    main()
