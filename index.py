#!/usr/bin/env python3
import api.cloudmon
import os
import sys
import tests.file_speedtest
import tests.network_speedtest


def main():
    print('Welcome!')
    print(sys.argv)
    api.cloudmon.send_results_to_cloud_mon('external_tests_has_started_on_' + os.getenv('CLOUD_MON_SERVER_ID'), 0)
    print('Now i will perform the tests.')
    print('First of all the network speed app')
    result = tests.network_speedtest.perform_test()
    print(result)
    # Network
    api.cloudmon.send_results_to_cloud_mon('speed_test_upload', result.upload)
    api.cloudmon.send_results_to_cloud_mon('speed_test_download', result.download)

    tests.file_speedtest.install_fio()
    file_speedtest_result = tests.file_speedtest.perform_test()
    print(file_speedtest_result)
    # FIO

    api.cloudmon.send_results_to_cloud_mon('disk_random_write', file_speedtest_result['random_write'])
    api.cloudmon.send_results_to_cloud_mon('disk_random_read', file_speedtest_result['random_read'])
    api.cloudmon.send_results_to_cloud_mon('disk_random_mixed_read', file_speedtest_result['mixed_rand_read'])
    api.cloudmon.send_results_to_cloud_mon('disk_random_mixed_write', file_speedtest_result['mixed_rand_write'])

    # Mark tests as done
    api.cloudmon.send_results_to_cloud_mon('external_tests_done_' + os.getenv('CLOUD_MON_SERVER_ID'), 0)
    print('Sendet!')



if __name__ == "__main__":
    main()
