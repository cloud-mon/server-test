#!/usr/bin/env python3
import api.cloudmon
import os
import sys
import tests.file_speedtest
import tests.network_speedtest


def main():
    print('Welcome!')
    print(sys.argv)
    if len(sys.argv) > 1:
        api_token = sys.argv[1]
    else:
        api_token = 'UNKNOWN'

    print(api_token)
    print('Now i will perform the tests.')
    print('First of all the network speed app')
    result = tests.network_speedtest.perform_test()
    print(result)

    tests.file_speedtest.install_fio()
    file_speedtest_result = tests.file_speedtest.perform_test()
    print(file_speedtest_result)
    if api_token != 'UNKNOWN':
        # Network
        api.cloudmon.send_results_to_cloud_mon('speed_test_upload', result.upload)
        api.cloudmon.send_results_to_cloud_mon('speed_test_download', result.download)

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
