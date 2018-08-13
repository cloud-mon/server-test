#!/usr/bin/env python3
import api.cloudmon
import os
import sys
import tests.file_speedtest
import tests.network_speedtest
import tests.cpu_speedtest
import tests.php_build_speedtest

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
    print('Perform FIO')
    tests.file_speedtest.install_fio()
    file_speedtest_result = tests.file_speedtest.perform_test()
    print(file_speedtest_result)
    # FIO

    api.cloudmon.send_results_to_cloud_mon('disk_random_write', file_speedtest_result['random_write'])
    api.cloudmon.send_results_to_cloud_mon('disk_random_read', file_speedtest_result['random_read'])
    api.cloudmon.send_results_to_cloud_mon('disk_random_mixed_read', file_speedtest_result['mixed_rand_read'])
    api.cloudmon.send_results_to_cloud_mon('disk_random_mixed_write', file_speedtest_result['mixed_rand_write'])

    print('Perform CPU Test')
    # CPU Test
    tests.cpu_speedtest.install_coremark()
    cpu_speedtest_result = tests.cpu_speedtest.perform_test()
    api.cloudmon.send_results_to_cloud_mon('cpu_iterations_per_sec', cpu_speedtest_result['iterations_per_sec'])

    if str(os.getenv('TEST_VOLUME_TOO')) == "1":
        print('Volume Speedtest')
        file_speedtest_result = tests.file_speedtest.perform_test(True)
        print(file_speedtest_result)
        # FIO on Volume

        api.cloudmon.send_results_to_cloud_mon('volume_random_write', file_speedtest_result['random_write'])
        api.cloudmon.send_results_to_cloud_mon('volume_random_read', file_speedtest_result['random_read'])
        api.cloudmon.send_results_to_cloud_mon('volume_random_mixed_read', file_speedtest_result['mixed_rand_read'])
        api.cloudmon.send_results_to_cloud_mon('volume_random_mixed_write', file_speedtest_result['mixed_rand_write'])

    print('Send Mark as "Ended" Request')
    print('Perform PHP Build Test')
    tests.php_build_speedtest.clone_php_src()
    php_build_test_result = tests.php_build_speedtest.perform_test()
    api.cloudmon.send_results_to_cloud_mon('real_world_php_build_time',php_build_test_result)
    
    # Mark tests as done
    api.cloudmon.send_results_to_cloud_mon('external_tests_done_' + os.getenv('CLOUD_MON_SERVER_ID'), 0)
    print('Sendet!')


if __name__ == "__main__":
    main()
